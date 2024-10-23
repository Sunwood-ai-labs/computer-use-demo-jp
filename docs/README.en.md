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
  ～ Claude 3.5 Sonnet Computer Use Functionality Demo ～

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
> The computer use functionality is in beta. Please note the following:
>
> 1. Run it with minimal privileges in a dedicated virtual machine or container.
> 2. Avoid accessing sensitive data or account information.
> 3. It is recommended to restrict internet access to only permitted domains.
> 4. Human verification is required for important operations or those requiring consent.

## 🚀 Project Overview

This repository provides a demo environment for testing the computer use functionality of Claude 3.5 Sonnet. Using a Streamlit application and a Docker container, it offers an agent loop that enables computer operation through the Anthropic API, AWS Bedrock, or Google Cloud Vertex AI.  Please use this according to the important security notes in the README.md.

## ✨ Key Features

- Support for Anthropic API, AWS Bedrock, and Google Cloud Vertex AI
- Environment setup using Docker containers
- Interactive operation via a Streamlit application
- Agent loop for computer operation
- File editing tool
- Computer operation tools (mouse, keyboard, screenshot operation, coordinate scaling function)
- Streamlit application (chat interface and desktop view, API key, provider, model, system prompt settings, agent loop execution, HTTP request log display, settings reset, image display/hide toggle)
- Bash tool (bash command execution, session management, timeout settings)
- Tool collection class capable of managing multiple tools
- Tool base class and result class to standardize tool creation and result processing
- Shell command execution utility
- HTTP server providing static content (IPv6 compatible)
- Scripts to start Xvfb, x11vnc, noVNC, Mutter, and Tint2 (with error handling and logging)


## 🔧 How to Use

1. **Select API Provider:** Choose your API provider (Anthropic, Bedrock, Vertex AI) from the `API Provider` radio button.
2. **Enter API Key/Credentials:** Follow the instructions in the sidebar to enter your API key or credentials for the selected API provider.
3. **Select Model (Optional):** You can specify the model to use. A default model is set.
4. **Run the Docker Container:** Follow the instructions in the Quick Start section to run the Docker container. (See the Dockerfile for Docker image build instructions.)
5. **Access the Application:** After starting the container, access the application at `http://localhost:8080`.


## 📦 Installation Instructions

1. **Install Docker:** Install Docker.
2. **Clone the Repository:** Clone this repository.
3. **Build the Docker Image:** Build the Docker image with `docker build . -t computer-use-demo`. Or, use a pre-built image. (See Dockerfile)
4. **Run the Container:** Run the Docker container according to the instructions in the Quick Start section.


## 🆕 What's New (Release v0.1.0)

![Release Header](https://raw.githubusercontent.com/Sunwood-ai-labs/computer-use-demo-jp/main/docs/release_notes/header_image/release_header_v0.1.0.png)

- Complete overhaul of the README file
- Addition and update of header image
- Update of the English README
- Addition of file editing tool and computer operation tools
- Several bug fixes
- Updates to related files due to repository name change


## 📄 License

This project is provided under the MIT License. See [LICENSE](LICENSE copy) for details.