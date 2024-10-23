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
  ～ Claude 3.5 Sonnet Computer Use Function Demo ～

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
> The computer use function is in beta. Please note the following:
>
> 1. Run it with minimal privileges in a dedicated virtual machine or container.
> 2. Avoid accessing sensitive data or account information.
> 3. It is recommended to restrict internet access to only permitted domains.
> 4. Human verification is required for important operations or those requiring consent.

## 🚀 Project Overview

This repository provides a demo environment for testing the computer use function of Claude 3.5 Sonnet.  Using a Streamlit application and a Docker container, it offers an agent loop enabling computer operations through the Anthropic API, AWS Bedrock, or Google Cloud Vertex AI.  Please use it according to the important security precautions listed in this README.md.

## ✨ Key Features

- Support for Anthropic API, AWS Bedrock, and Google Cloud Vertex AI.
- Environment setup using a Docker container.
- Interactive operation via a Streamlit application.
- Agent loop for computer operations.


## 🔧 How to Use

1.  **Select API Provider:** Select the API provider (Anthropic, Bedrock, Vertex AI) to use from the `API Provider` radio button.
2.  **Enter API Key/Credentials:** Enter the API key or credentials for the selected API provider according to the instructions displayed in the sidebar.
3.  **Select Model (Optional):** You can specify the model to use. A default model is set.
4.  **Run the Docker Container:** Follow the instructions in the Quick Start section to run the Docker container.
5.  **Access the Application:** After the container starts, access the application at `http://localhost:8080`.

## 📦 Installation Instructions

1.  **Install Docker:** Install Docker.
2.  **Clone the Repository:** Clone this repository.
3.  **Build the Docker Image (Optional):** Build the Docker image with `docker build . -t computer-use-demo`. The Quick Start section also shows how to use a pre-built image.
4.  **Run the Container:** Follow the instructions in the Quick Start section to run the Docker container.


## 🆕 Latest Information (Release v0.0.0)

![Release Header](https://raw.githubusercontent.com/Sunwood-ai-labs/computer-use-demo-jp/main/docs/release_notes/header_image/release_header_v0.0.0.png)

- This release is the initial v0.0.0 release and is in beta.  Please be sure to read the security precautions listed in the README.md.


## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE copy) for details.