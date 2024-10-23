<p align="center">
  <img src="https://raw.githubusercontent.com/Sunwood-ai-labs/computer-use-demo-jp/refs/heads/main/docs/computer-use-demo.png" width="100%">
  <h1 align="center">🌟 Anthropic Computer Use Demo 🌟</h1>
</p>

<p align="center">
  <a href="https://github.com/anthropics/computer-use-demo">
    <img alt="GitHub Repo" src="https://img.shields.io/badge/github-computer--use--demo-blue?logo=github">
  </a>
  <a href="https://github.com/anthropics/computer-use-demo/blob/main/LICENSE">
    <img alt="License" src="https://img.shields.io/github/license/anthropics/computer-use-demo?color=green">
  </a>
  <a href="https://github.com/anthropics/computer-use-demo/stargazers">
    <img alt="GitHub stars" src="https://img.shields.io/github/stars/anthropics/computer-use-demo?style=social">
  </a>
</p>

<h2 align="center">
  ～ Claude 3.5 Sonnetのコンピューター使用機能デモ ～

<a href="https://github.com/anthropics/computer-use-demo/blob/main/README.md"><img src="https://img.shields.io/badge/ドキュメント-日本語-white.svg" alt="JA doc"/></a>
<a href="https://github.com/anthropics/computer-use-demo/blob/main/docs/README.en.md"><img src="https://img.shields.io/badge/english-document-white.svg" alt="EN doc"></a>
</h2>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker" alt="Docker">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit" alt="Streamlit">
  <img src="https://img.shields.io/badge/Anthropic-6B4FBB?style=for-the-badge" alt="Anthropic">
</p>

> [!CAUTION]
> コンピューター使用機能はベータ版です。以下の点に注意してください：
>
> 1. 専用の仮想マシンやコンテナで最小限の権限で実行してください
> 2. センシティブなデータやアカウント情報へのアクセスを避けてください
> 3. インターネットアクセスは許可ドメインのみに制限することを推奨します
> 4. 重要な操作や同意が必要な操作は人間が確認してください

## 🚀 プロジェクト概要

このリポジトリは、Claude 3.5 Sonnetのコンピューター使用機能を試すためのデモ環境を提供します。以下の要素が含まれています：

- 必要な依存関係を含むDockerコンテナ
- Anthropic API、Bedrock、またはVertexを使用したエージェントループ
- Anthropic定義のコンピューター使用ツール
- インタラクティブなStreamlitアプリケーション

## 🆕 クイックスタート

### Anthropic API使用

```bash
export ANTHROPIC_API_KEY=%your_api_key%
docker run \
    -e ANTHROPIC_API_KEY=$ANTHROPIC_API_KEY \
    -v $HOME/.anthropic:/home/computeruse/.anthropic \
    -p 5900:5900 \
    -p 8501:8501 \
    -p 6080:6080 \
    -p 8080:8080 \
    -it ghcr.io/anthropics/anthropic-quickstarts:computer-use-demo-latest
```

```powershell
docker run `
    -e ANTHROPIC_API_KEY=$env:ANTHROPIC_API_KEY `
    -v "${HOME}/.anthropic:/home/computeruse/.anthropic" `
    -p 5900:5900 `
    -p 8501:8501 `
    -p 6080:6080 `
    -p 8080:8080 `
    -it ghcr.io/anthropics/anthropic-quickstarts:computer-use-demo-latest
```

### AWS Bedrock使用

AWSの認証方法として以下のオプションがあります：

#### オプション1: AWSクレデンシャルファイルとプロファイルを使用（推奨）

```bash
export AWS_PROFILE=<your_aws_profile>
docker run \
    -e API_PROVIDER=bedrock \
    -e AWS_PROFILE=$AWS_PROFILE \
    -e AWS_REGION=us-west-2 \
    -v $HOME/.aws/credentials:/home/computeruse/.aws/credentials \
    -v $HOME/.anthropic:/home/computeruse/.anthropic \
    -p 5900:5900 \
    -p 8501:8501 \
    -p 6080:6080 \
    -p 8080:8080 \
    -it ghcr.io/anthropics/anthropic-quickstarts:computer-use-demo-latest
```

#### オプション2: アクセスキーとシークレットを使用

```bash
export AWS_ACCESS_KEY_ID=%your_aws_access_key%
export AWS_SECRET_ACCESS_KEY=%your_aws_secret_access_key%
export AWS_SESSION_TOKEN=%your_aws_session_token%
docker run \
    -e API_PROVIDER=bedrock \
    -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
    -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
    -e AWS_SESSION_TOKEN=$AWS_SESSION_TOKEN \
    -e AWS_REGION=us-west-2 \
    -v $HOME/.anthropic:/home/computeruse/.anthropic \
    -p 5900:5900 \
    -p 8501:8501 \
    -p 6080:6080 \
    -p 8080:8080 \
    -it ghcr.io/anthropics/anthropic-quickstarts:computer-use-demo-latest
```

### Google Cloud Vertex AI使用

```bash
docker build . -t computer-use-demo
gcloud auth application-default login
export VERTEX_REGION=%your_vertex_region%
export VERTEX_PROJECT_ID=%your_vertex_project_id%
docker run \
    -e API_PROVIDER=vertex \
    -e CLOUD_ML_REGION=$VERTEX_REGION \
    -e ANTHROPIC_VERTEX_PROJECT_ID=$VERTEX_PROJECT_ID \
    -v $HOME/.config/gcloud/application_default_credentials.json:/home/computeruse/.config/gcloud/application_default_credentials.json \
    -p 5900:5900 \
    -p 8501:8501 \
    -p 6080:6080 \
    -p 8080:8080 \
    -it computer-use-demo
```

## 📺 デモアプリへのアクセス

コンテナ起動後、以下のURLでアクセスできます：

- 統合インターフェース: [http://localhost:8080](http://localhost:8080)
- Streamlitインターフェースのみ: [http://localhost:8501](http://localhost:8501)
- デスクトップビューのみ: [http://localhost:6080/vnc.html](http://localhost:6080/vnc.html)
- VNC直接接続: `vnc://localhost:5900`

## 🖥️ スクリーンサイズの設定

環境変数 `WIDTH` と `HEIGHT` でスクリーンサイズを設定できます：

```bash
docker run \
    -e ANTHROPIC_API_KEY=$ANTHROPIC_API_KEY \
    -v $HOME/.anthropic:/home/computeruse/.anthropic \
    -p 5900:5900 \
    -p 8501:8501 \
    -p 6080:6080 \
    -p 8080:8080 \
    -e WIDTH=1920 \
    -e HEIGHT=1080 \
    -it ghcr.io/anthropics/anthropic-quickstarts:computer-use-demo-latest
```

> [!IMPORTANT]
> パフォーマンスと精度の観点から、[XGA/WXGA](https://en.wikipedia.org/wiki/Display_resolution_standards#XGA)以上の解像度でのスクリーンショット送信は推奨されません。

## 🛠️ 開発環境のセットアップ

```bash
./setup.sh  # 仮想環境の設定、開発依存関係のインストール、pre-commitフックの設定
docker build . -t computer-use-demo:local  # Dockerイメージの手動ビルド（任意）
export ANTHROPIC_API_KEY=%your_api_key%
docker run \
    -e ANTHROPIC_API_KEY=$ANTHROPIC_API_KEY \
    -v $(pwd)/computer_use_demo:/home/computeruse/computer_use_demo/ \
    -v $HOME/.anthropic:/home/computeruse/.anthropic \
    -p 5900:5900 \
    -p 8501:8501 \
    -p 6080:6080 \
    -p 8080:8080 \
    -it computer-use-demo:local
```

## 🤝 フィードバック

ベータ版の品質向上のため、[こちらのフォーム](https://forms.gle/BT1hpBrqDPDUrCqo7)からフィードバックをお寄せください。モデルの応答品質、API、ドキュメントについてのご意見をお待ちしています！

## 📄 ライセンス

本プロジェクトはMITライセンスで提供されています。詳細は[LICENSE](LICENSE)をご覧ください。
