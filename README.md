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

このリポジトリは、Claude 3.5 Sonnetのコンピューター使用機能を試すためのデモ環境を提供します。StreamlitアプリケーションとDockerコンテナを使用して、Anthropic API、AWS Bedrock、またはGoogle Cloud Vertex AIを通じて、コンピューター操作を可能にするエージェントループを提供します。README.mdに記載されている重要なセキュリティ上の注意事項に従って使用してください。

## ✨ 主な機能

- Anthropic API、AWS Bedrock、Google Cloud Vertex AIへの対応
- Dockerコンテナによる環境構築
- Streamlitアプリケーションによるインタラクティブな操作
- コンピューター操作のためのエージェントループ


## 🔧 使用方法

1.  **APIプロバイダーを選択:**  `API Provider`ラジオボタンから、使用するAPIプロバイダー(Anthropic, Bedrock, Vertex AI)を選択します。
2.  **APIキー/認証情報の入力:** サイドバーに表示される指示に従い、選択したAPIプロバイダーのAPIキーまたは認証情報を入力します。
3.  **モデルの選択 (オプション):** 使用するモデルを指定できます。デフォルトモデルが設定されています。
4.  **Dockerコンテナの実行:** クイックスタートセクションの指示に従い、Dockerコンテナを実行します。
5.  **アプリケーションへのアクセス:** コンテナ起動後、`http://localhost:8080`にアクセスしてアプリケーションを使用します。

## 📦 インストール手順

1.  **Dockerのインストール:** Dockerをインストールします。
2.  **リポジトリのクローン:** このリポジトリをクローンします。
3.  **Dockerイメージのビルド (オプション):**  `docker build . -t computer-use-demo`でDockerイメージをビルドします。クイックスタートセクションでは、事前にビルド済みのイメージを使用する方法も示しています。
4.  **コンテナの実行:** クイックスタートセクションの指示に従って、Dockerコンテナを実行します。


## 🆕 最新情報 (Release v0.0.0)

![Release Header](https://raw.githubusercontent.com/Sunwood-ai-labs/computer-use-demo-jp/main/docs/release_notes/header_image/release_header_v0.0.0.png)

- このリリースはv0.0.0の初期リリースであり、ベータ版です。README.mdに記載されているセキュリティに関する注意事項を必ずお読みください。


## 📄 ライセンス

本プロジェクトはMITライセンスで提供されています。詳細は[LICENSE](LICENSE copy)をご覧ください。