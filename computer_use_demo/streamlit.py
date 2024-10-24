"""
Streamlitのエントリーポイント、詳細は https://docs.streamlit.io/ を参照
"""

import asyncio
import base64
import os
import subprocess
from datetime import datetime
from enum import StrEnum
from functools import partial
from pathlib import PosixPath
from typing import cast

import streamlit as st
from anthropic import APIResponse
from anthropic.types import (
    TextBlock,
)
from anthropic.types.beta import BetaMessage, BetaTextBlock, BetaToolUseBlock
from anthropic.types.tool_use_block import ToolUseBlock
from streamlit.delta_generator import DeltaGenerator

from computer_use_demo.loop import (
    PROVIDER_TO_DEFAULT_MODEL_NAME,
    APIProvider,
    sampling_loop,
)
from computer_use_demo.tools import ToolResult

CONFIG_DIR = PosixPath("~/.anthropic").expanduser()
API_KEY_FILE = CONFIG_DIR / "api_key"
STREAMLIT_STYLE = """
<style>
    /* エージェントループ実行中はチャット入力を非表示 */
    .stApp[data-teststate=running] .stChatInput textarea,
    .stApp[data-test-script-state=running] .stChatInput textarea {
        display: none;
    }
     /* Streamlitのデプロイボタンを非表示 */
    .stDeployButton {
        visibility: hidden;
    }
</style>
"""

WARNING_TEXT = "⚠️ セキュリティ警告: 悪意のあるウェブコンテンツがClaudeの動作を乗っ取る可能性があるため、機密アカウントやデータへのアクセスは絶対に提供しないでください"


class Sender(StrEnum):
    USER = "user"
    BOT = "assistant"
    TOOL = "tool"


def setup_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "api_key" not in st.session_state:
        # まずファイルからAPIキーを読み込み、次に環境変数から読み込む
        st.session_state.api_key = load_from_storage("api_key") or os.getenv(
            "ANTHROPIC_API_KEY", ""
        )
    if "provider" not in st.session_state:
        st.session_state.provider = (
            os.getenv("API_PROVIDER", "anthropic") or APIProvider.ANTHROPIC
        )
    if "provider_radio" not in st.session_state:
        st.session_state.provider_radio = st.session_state.provider
    if "model" not in st.session_state:
        _reset_model()
    if "auth_validated" not in st.session_state:
        st.session_state.auth_validated = False
    if "responses" not in st.session_state:
        st.session_state.responses = {}
    if "tools" not in st.session_state:
        st.session_state.tools = {}
    if "only_n_most_recent_images" not in st.session_state:
        st.session_state.only_n_most_recent_images = 10
    if "custom_system_prompt" not in st.session_state:
        st.session_state.custom_system_prompt = load_from_storage("system_prompt") or ""
    if "hide_images" not in st.session_state:
        st.session_state.hide_images = False


def _reset_model():
    st.session_state.model = PROVIDER_TO_DEFAULT_MODEL_NAME[
        cast(APIProvider, st.session_state.provider)
    ]


async def main():
    """Streamlitのレンダリングループ"""
    setup_state()

    st.markdown(STREAMLIT_STYLE, unsafe_allow_html=True)

    st.title("Claude コンピュータ操作デモ")

    if not os.getenv("HIDE_WARNING", False):
        st.warning(WARNING_TEXT)

    with st.sidebar:

        def _reset_api_provider():
            if st.session_state.provider_radio != st.session_state.provider:
                _reset_model()
                st.session_state.provider = st.session_state.provider_radio
                st.session_state.auth_validated = False

        provider_options = [option.value for option in APIProvider]
        st.radio(
            "APIプロバイダー",
            options=provider_options,
            key="provider_radio",
            format_func=lambda x: x.title(),
            on_change=_reset_api_provider,
        )

        st.text_input("モデル", key="model")

        if st.session_state.provider == APIProvider.ANTHROPIC:
            st.text_input(
                "Anthropic APIキー",
                type="password",
                key="api_key",
                on_change=lambda: save_to_storage("api_key", st.session_state.api_key),
            )

        st.number_input(
            "直近N枚の画像のみ送信",
            min_value=0,
            key="only_n_most_recent_images",
            help="総トークン数を減らすため、古いスクリーンショットを会話から削除します",
        )
        st.text_area(
            "カスタムシステムプロンプトの接尾辞",
            key="custom_system_prompt",
            help="システムプロンプトに追加する指示。基本のシステムプロンプトについては computer_use_demo/loop.py を参照してください。",
            on_change=lambda: save_to_storage(
                "system_prompt", st.session_state.custom_system_prompt
            ),
        )
        st.checkbox("スクリーンショットを非表示", key="hide_images")

        if st.button("リセット", type="primary"):
            with st.spinner("リセット中..."):
                st.session_state.clear()
                setup_state()

                subprocess.run("pkill Xvfb; pkill tint2", shell=True)  # noqa: ASYNC221
                await asyncio.sleep(1)
                subprocess.run("./start_all.sh", shell=True)  # noqa: ASYNC221

    if not st.session_state.auth_validated:
        if auth_error := validate_auth(
            st.session_state.provider, st.session_state.api_key
        ):
            st.warning(f"以下の認証の問題を解決してください:\n\n{auth_error}")
            return
        else:
            st.session_state.auth_validated = True

    chat, http_logs = st.tabs(["チャット", "HTTP通信ログ"])
    new_message = st.chat_input(
        "コンピュータを操作するためのメッセージをClaudeに送信..."
    )

    with chat:
        # 過去のチャットを表示
        for message in st.session_state.messages:
            if isinstance(message["content"], str):
                _render_message(message["role"], message["content"])
            elif isinstance(message["content"], list):
                for block in message["content"]:
                    # Anthropic APIに送り返すツール実行結果だけでは全ての詳細を表示するのに不十分なため、
                    # ツール使用の応答を保存しています
                    if isinstance(block, dict) and block["type"] == "tool_result":
                        _render_message(
                            Sender.TOOL, st.session_state.tools[block["tool_use_id"]]
                        )
                    else:
                        _render_message(
                            message["role"],
                            cast(BetaTextBlock | BetaToolUseBlock, block),
                        )

        # 過去のHTTP通信を表示
        for identity, response in st.session_state.responses.items():
            _render_api_response(response, identity, http_logs)

        # 新しいチャットを表示
        if new_message:
            st.session_state.messages.append(
                {
                    "role": Sender.USER,
                    "content": [TextBlock(type="text", text=new_message)],
                }
            )
            _render_message(Sender.USER, new_message)

        try:
            most_recent_message = st.session_state["messages"][-1]
        except IndexError:
            return

        if most_recent_message["role"] is not Sender.USER:
            # 応答すべきユーザーメッセージがない場合は終了
            return

        with st.spinner("エージェントを実行中..."):
            # 最新のメッセージでエージェントのサンプリングループを実行
            st.session_state.messages = await sampling_loop(
                system_prompt_suffix=st.session_state.custom_system_prompt,
                model=st.session_state.model,
                provider=st.session_state.provider,
                messages=st.session_state.messages,
                output_callback=partial(_render_message, Sender.BOT),
                tool_output_callback=partial(
                    _tool_output_callback, tool_state=st.session_state.tools
                ),
                api_response_callback=partial(
                    _api_response_callback,
                    tab=http_logs,
                    response_state=st.session_state.responses,
                ),
                api_key=st.session_state.api_key,
                only_n_most_recent_images=st.session_state.only_n_most_recent_images,
            )


def validate_auth(provider: APIProvider, api_key: str | None):
    if provider == APIProvider.ANTHROPIC:
        if not api_key:
            return "続行するには、サイドバーでAnthropic APIキーを入力してください。"
    if provider == APIProvider.BEDROCK:
        import boto3

        if not boto3.Session().get_credentials():
            return "Bedrock APIを使用するにはAWSクレデンシャルを設定する必要があります。"
    if provider == APIProvider.VERTEX:
        import google.auth
        from google.auth.exceptions import DefaultCredentialsError

        if not os.environ.get("CLOUD_ML_REGION"):
            return "Vertex APIを使用するにはCLOUD_ML_REGION環境変数を設定してください。"
        try:
            google.auth.default(
                scopes=["https://www.googleapis.com/auth/cloud-platform"],
            )
        except DefaultCredentialsError:
            return "Google Cloudクレデンシャルが正しく設定されていません。"


def load_from_storage(filename: str) -> str | None:
    """ストレージディレクトリからデータを読み込む"""
    try:
        file_path = CONFIG_DIR / filename
        if file_path.exists():
            data = file_path.read_text().strip()
            if data:
                return data
    except Exception as e:
        st.write(f"デバッグ: {filename}の読み込み中にエラーが発生: {e}")
    return None


def save_to_storage(filename: str, data: str) -> None:
    """ストレージディレクトリにデータを保存する"""
    try:
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        file_path = CONFIG_DIR / filename
        file_path.write_text(data)
        # ユーザーのみが読み書き可能なようにファイルのパーミッションを設定
        file_path.chmod(0o600)
    except Exception as e:
        st.write(f"デバッグ: {filename}の保存中にエラーが発生: {e}")


def _api_response_callback(
    response: APIResponse[BetaMessage],
    tab: DeltaGenerator,
    response_state: dict[str, APIResponse[BetaMessage]],
):
    """
    APIレスポンスを状態に保存し、表示する
    """
    response_id = datetime.now().isoformat()
    response_state[response_id] = response
    _render_api_response(response, response_id, tab)


def _tool_output_callback(
    tool_output: ToolResult, tool_id: str, tool_state: dict[str, ToolResult]
):
    """ツール出力を状態に保存し、表示する"""
    tool_state[tool_id] = tool_output
    _render_message(Sender.TOOL, tool_output)


def _render_api_response(
    response: APIResponse[BetaMessage], response_id: str, tab: DeltaGenerator
):
    """APIレスポンスをStreamlitのタブに表示する"""
    with tab:
        with st.expander(f"リクエスト/レスポンス ({response_id})"):
            newline = "\n\n"
            st.markdown(
                f"`{response.http_request.method} {response.http_request.url}`{newline}{newline.join(f'`{k}: {v}`' for k, v in response.http_request.headers.items())}"
            )
            st.json(response.http_request.read().decode())
            st.markdown(
                f"`{response.http_response.status_code}`{newline}{newline.join(f'`{k}: {v}`' for k, v in response.headers.items())}"
            )
            st.json(response.http_response.text)


def _render_message(
    sender: Sender,
    message: str | BetaTextBlock | BetaToolUseBlock | ToolResult,
):
    """ユーザーからの入力またはエージェントからの出力をStreamlitメッセージに変換する"""
    # Streamlitのホットリロードがisinstance検査を壊すため、クラス名をチェックする必要がある
    is_tool_result = not isinstance(message, str) and (
        isinstance(message, ToolResult)
        or message.__class__.__name__ == "ToolResult"
        or message.__class__.__name__ == "CLIResult"
    )
    if not message or (
        is_tool_result
        and st.session_state.hide_images
        and not hasattr(message, "error")
        and not hasattr(message, "output")
    ):
        return
    with st.chat_message(sender):
        if is_tool_result:
            message = cast(ToolResult, message)
            if message.output:
                if message.__class__.__name__ == "CLIResult":
                    st.code(message.output)
                else:
                    st.markdown(message.output)
            if message.error:
                st.error(message.error)
            if message.base64_image and not st.session_state.hide_images:
                st.image(base64.b64decode(message.base64_image))
        elif isinstance(message, BetaTextBlock) or isinstance(message, TextBlock):
            st.write(message.text)
        elif isinstance(message, BetaToolUseBlock) or isinstance(message, ToolUseBlock):
                    st.code(f"ツール使用: {message.name}\n入力: {message.input}")
        else:
            st.markdown(message)


if __name__ == "__main__":
    asyncio.run(main())
