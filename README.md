<p align="center">
  <img src="https://raw.githubusercontent.com/Sunwood-ai-labs/computer-use-demo-jp/refs/heads/main/docs/computer-use-demo.png" width="100%">
  <h1 align="center">🌟 Anthropic Computer Use Demo (Japanese) 🌟</h1>
</p>

<p align="center">
  <a href="https://github.com/Sunwood-ai-labs/computer-use-demo-jp">
    <img alt="GitHub Repo" src="https://img.shields.io/badge/github-computer--use--demo-jp-blue?logo=github">
  </a>
  <a href="https://github.com/Sunwood-ai-labs/computer-use-demo-jp/blob/main/LICENSE%20copy">
    <img alt="License" src="https://img.shields.io/github/license/Sunwood-ai-labs/computer-use-demo-jp?color=green">
  </a>
  <a href="https://github.com/Sunwood-ai-labs/computer-use-demo-jp/stargazers">
    <img alt="GitHub stars" src="https://img.shields.io/github/stars/Sunwood-ai-labs/computer-use-demo-jp?style=social">
  </a>
</p>

<h2 align="center">
  ～ Claude 3.5 Sonnetのコンピューター使用機能デモ ～

<a href="https://github.com/Sunwood-ai-labs/computer-use-demo-jp/blob/main/README.md"><img src="https://img.shields.io/badge/ドキュメント-日本語-white.svg" alt="JA doc"/></a>
<a href="https://github.com/Sunwood-ai-labs/computer-use-demo-jp/blob/main/docs/README.en.md"><img src="https://img.shields.io/badge/english-document-white.svg" alt="EN doc"></a>
</h2>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker" alt="Docker">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit" alt="Streamlit">
  <img src="https://img.shields.io/badge/Anthropic-6B4FBB?style=for-the-badge" alt="Anthropic">
</p>

>  [!CAUTION]
> Computer useは現在ベータ機能です。Computer useは、標準的なAPIやチャットインターフェースとは異なる固有のリスクがあることにご注意ください。特にインターネットとの対話を行う場合、これらのリスクは高まります。リスクを最小限に抑えるため、以下のような予防措置を検討してください：
>
> 1. システムへの直接的な攻撃や事故を防ぐため、最小限の権限を持つ専用の仮想マシンまたはコンテナを使用する
> 2. 情報漏洩を防ぐため、アカウントのログイン情報などの機密データへのアクセスを制限する
> 3. 悪意のあるコンテンツへの露出を減らすため、許可リストに登録されたドメインのみにインターネットアクセスを制限する
> 4. クッキーの承認、金融取引、利用規約への同意など、実世界で重要な結果をもたらす可能性のある決定や、明示的な同意を必要とするタスクについては、人間による確認を求める
>
> 場合によっては、Claudeはユーザーの指示と矛盾する内容であっても、コンテンツ内のコマンドに従う可能性があります。例えば、ウェブページや画像に含まれる指示がユーザーの指示を上書きしたり、Claudeにエラーを引き起こす可能性があります。プロンプトインジェクションに関連するリスクを避けるため、機密データやアクションからClaudeを隔離することをお勧めします。
>
> 最後に、自社製品でcomputer useを有効にする前に、エンドユーザーに関連するリスクを通知し、同意を得てください。

このリポジトリは、Claudeのcomputer useを開始するための以下の参照実装を提供します：

* 必要な依存関係を含むDockerコンテナを作成するためのビルドファイル
* Anthropic API、Bedrock、またはVertexを使用してClaude 3.5 Sonnetモデルにアクセスするcomputer useエージェントループ
* Anthropicが定義したcomputer useツール
* エージェントループと対話するためのStreamlitアプリ

モデルの応答品質、API自体、またはドキュメントの品質についてのフィードバックは[このフォーム](https://forms.gle/BT1hpBrqDPDUrCqo7)からお寄せください。

> [!IMPORTANT]
> この参照実装で使用されているベータAPIは変更される可能性があります。最新の情報については[APIリリースノート](https://docs.anthropic.com/en/release-notes/api)を参照してください。

> [!IMPORTANT]
> コンポーネントは緩やかに分離されています：エージェントループはClaudeによって制御されるコンテナ内で実行され、一度に1つのセッションでのみ使用でき、必要に応じてセッション間で再起動またはリセットする必要があります。

## 🚀 クイックスタート：Dockerコンテナの実行

### 🔑 Anthropic APIキーを用いた実行

> [!TIP]
> APIキーは[Anthropic Console](https://console.anthropic.com/)で確認できます。

```bash
export ANTHROPIC_API_KEY=%your_api_key%
docker compose up -d
```

コンテナが起動したら、インターフェースへの接続方法については下記の[デモアプリへのアクセス](#デモアプリへのアクセス)セクションを参照してください。


### 🖥️ デモアプリへのアクセス

コンテナが起動したら、ブラウザで[http://localhost:8080](http://localhost:8080)を開いて、エージェントチャットとデスクトップビューの両方を含む統合インターフェースにアクセスできます。

コンテナはAPIキーやカスタムシステムプロンプトなどの設定を`~/.anthropic/`に保存します。これらの設定をコンテナの実行間で保持するには、このディレクトリをマウントしてください。

その他のアクセスポイント：

- Streamlitインターフェースのみ：[http://localhost:8501](http://localhost:8501)
- デスクトップビューのみ：[http://localhost:6080/vnc.html](http://localhost:6080/vnc.html)
- 直接VNC接続：`vnc://localhost:5900`（VNCクライアント用）

## 📏 画面サイズ

環境変数`WIDTH`と`HEIGHT`を使用して画面サイズを設定できます。例：

```bash
export WIDTH=1920
export HEIGHT=1080
docker compose up -d
```

[画像のリサイズ](https://docs.anthropic.com/en/docs/build-with-claude/vision#evaluate-image-size)に関する問題を避けるため、[XGA/WXGA](https://en.wikipedia.org/wiki/Display_resolution_standards#XGA)以上の解像度でのスクリーンショット送信はお勧めしません。
APIの画像リサイズ動作に依存すると、ツールで直接スケーリングを実装する場合と比べて、モデルの精度が低下しパフォーマンスが遅くなります。このプロジェクトの`computer`ツール実装では、より高い解像度から推奨解像度への画像とコーディネートのスケーリング方法を示しています。

## 🛠️ 開発環境

```bash
./setup.sh  # venvの設定、開発依存関係のインストール、pre-commitフックのインストール
docker build . -t computer-use-demo:local  # Dockerイメージを手動でビルド（オプション）
export ANTHROPIC_API_KEY=%your_api_key%
docker compose up -d
```

```powershell
# Dockerイメージを手動でビルド（オプション）
docker build . -t computer-use-demo:local

# 環境変数の設定
$env:ANTHROPIC_API_KEY = "your_api_key"

# Dockerコンテナの実行
docker compose up -d
```

上記のdocker runコマンドは、ホストから編集できるようにリポジトリをDockerイメージ内にマウントします。Streamlitは自動リロードが既に設定されています。

## 📂 リポジトリの詳細構造

以下に、主要なディレクトリとファイルの役割を詳しく説明します。

### 🗄️ 主要ディレクトリ

* **`computer_use_demo/`**: AIエージェントの頭脳を構成するPythonコードの中核部分。
    * **`tools/`**: AIエージェントが使用するツール群を実装。`bash.py` (bashコマンド実行), `computer.py` (画面/キーボード/マウス操作), `edit.py` (ファイル編集)など、各ツールは特定の機能を提供します。`base.py`はツールの基底クラスを定義し、`collection.py`はツール群を一括管理します。`run.py`はシェルコマンドの非同期実行ユーティリティを提供します。
    * `loop.py`: AIエージェントとの対話ループを実装。API呼び出し、ツールの実行、結果の処理などを繰り返すことで、AIエージェントが自律的に動作します。
    * `requirements.txt`: デモ実行に必要なPythonパッケージをリストアップします。
    * `streamlit.py`: Streamlitアプリのエントリポイント。ユーザーインターフェースを提供し、チャット画面、API通信ログ表示、設定パネルなどを表示します。
* **`image/`**: Dockerイメージ構築に必要なファイル群。仮想環境の設計図と言えるでしょう。
    * `static_content/`: HTTPサーバーが提供するHTML, JavaScript等の静的コンテンツ。StreamlitアプリとnoVNCを統合したインターフェースを提供します。
    * `entrypoint.sh`: Dockerコンテナ起動時に実行されるスクリプト。各種サービスの起動とログの設定などを行います。
    * `http_server.py`: StreamlitとnoVNCへのアクセスを統合するシンプルなHTTPサーバー。
    * `*.startup.sh`: Xvfb (仮想ディスプレイ), tint2 (パネル), mutter (ウィンドウマネージャ), x11vnc (VNCサーバー), noVNC (HTML5 VNCクライアント) などの起動スクリプト。
    * `.config/`: tint2の設定ファイル等。

### 📄 その他のファイル

* `.env.example`: 環境変数の設定例。APIキーや各種トークンの設定に使用します。
* `app.py`: シンプルなStreamlitアプリでREADME.mdの内容を表示します。
* `dev-requirements.txt`: 開発環境に必要なパッケージ一覧。
* `Dockerfile`: Dockerイメージの構築方法を定義。Ubuntuベースのイメージに必要ツールやライブラリをインストールし、ユーザー、Python環境、デスクトップ環境をセットアップします。
* `LICENSE copy`: ライセンス情報。
* `pyproject.toml`: プロジェクト設定ファイル。Pyrightとpytestの設定が含まれています。
* `README.md`: プロジェクトの説明ドキュメント。
* `requirements.txt`: 実行に必要なPythonパッケージ一覧。
* `ruff.toml`: Ruff (Pythonのlinter) の設定ファイル。
* `setup.ps1`, `setup.sh`: 開発環境のセットアップスクリプト。Windows (PowerShell) とLinux/macOS (bash) に対応しています。


### 📊 リポジトリ構造の可視化

```mermaid
%%{init: {'theme':'base'}}%%

graph LR
    subgraph computer_use_demo_files
        tools --> base.py
        tools --> bash.py
        tools --> computer.py
        tools --> edit.py
        tools --> collection.py
        tools --> run.py
        demo_root --> loop.py
        demo_root --> requirements.txt
        demo_root --> streamlit.py
    end

    subgraph image_files
        image --> static_content
        static_content --> index.html
        image --> entrypoint.sh
        image --> http_server.py
        image --> *.startup.sh
        image --> .config
    end

    Root --> computer_use_demo
    Root --> image
    Root --> Dockerfile
    Root --> README.md
    Root --> requirements.txt
```

## 📄 ライセンス

📄 MIT License

## 👏 謝辞

iris-s-coon、Maki

