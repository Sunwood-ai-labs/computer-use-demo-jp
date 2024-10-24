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
> Computer use is currently a beta feature.  Please be aware that computer use has inherent risks that differ from standard APIs and chat interfaces. These risks are particularly heightened when interacting with the internet. To minimize risk, consider preventative measures such as:
>
> 1. Using a dedicated virtual machine or container with minimal privileges to prevent direct attacks or accidents on your system.
> 2. Restricting access to sensitive data, such as account login credentials, to prevent information leaks.
> 3. Limiting internet access to only whitelisted domains to reduce exposure to malicious content.
> 4. Seeking human confirmation for decisions that could have significant real-world consequences, such as cookie approvals, financial transactions, or agreeing to terms of service, and for tasks requiring explicit consent.
>
> In some cases, Claude may follow commands within content even if they contradict user instructions. For example, instructions embedded in web pages or images may override user instructions or cause errors in Claude. To mitigate risks associated with prompt injection, it is recommended to isolate Claude from sensitive data and actions.
>
> Finally, before enabling computer use in your product, notify and obtain consent from your end-users regarding the associated risks.

This repository provides the following reference implementation for getting started with Claude's computer use:

* Build files to create a Docker container with necessary dependencies.
* A computer use agent loop that accesses the Claude 3.5 Sonnet model using the Anthropic API, Bedrock, or Vertex.
* Anthropic-defined computer use tools.
* A Streamlit app for interacting with the agent loop.

Feedback on model response quality, the API itself, or the quality of the documentation can be submitted via [this form](https://forms.gle/BT1hpBrqDPDUrCqo7).

> [!IMPORTANT]
> The beta APIs used in this reference implementation are subject to change. Refer to the [API release notes](https://docs.anthropic.com/en/release-notes/api) for the latest information.

> [!IMPORTANT]
> Components are loosely coupled: the agent loop runs within a container controlled by Claude, is usable only in one session at a time, and needs to be restarted or reset between sessions as needed.

## Quickstart: Running the Docker Container

### Anthropic API

> [!TIP]
> Your API key can be found in the [Anthropic Console](https://console.anthropic.com/).

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

Once the container is running, see the [Accessing the Demo App](#accessing-the-demo-app) section below for how to connect to the interface.

### Bedrock

To use Claude with Bedrock, you need to pass AWS credentials with appropriate permissions.

There are multiple options for authentication with Bedrock.  See the [boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#environment-variables) for details and options.

#### Option 1: (Recommended) Using host's AWS credentials file and AWS profile

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

Once the container is running, see the [Accessing the Demo App](#accessing-the-demo-app) section below for how to connect to the interface.

#### Option 2: Using access key and secret

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

Once the container is running, see the [Accessing the Demo App](#accessing-the-demo-app) section below for how to connect to the interface.

### Vertex

To use Claude with Vertex, you need to pass Google Cloud credentials with appropriate permissions.

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

Once the container is running, see the [Accessing the Demo App](#accessing-the-demo-app) section below for how to connect to the interface.

This example shows authentication using Google Cloud Application Default Credentials with Vertex.

You can also set `GOOGLE_APPLICATION_CREDENTIALS` to use an arbitrary credentials file. See the [Google Cloud authentication documentation](https://cloud.google.com/docs/authentication/application-default-credentials#GAC) for details.

### Accessing the Demo App

Once the container is running, open [http://localhost:8080](http://localhost:8080) in your browser to access the integrated interface, including both the agent chat and desktop view.

The container saves settings such as API keys and custom system prompts to `~/.anthropic/`. To persist these settings between container runs, mount this directory.

Other access points:

- Streamlit interface only: [http://localhost:8501](http://localhost:8501)
- Desktop view only: [http://localhost:6080/vnc.html](http://localhost:6080/vnc.html)
- Direct VNC connection: `vnc://localhost:5900` (for VNC clients)

## Screen Size

You can set the screen size using environment variables `WIDTH` and `HEIGHT`. Example:

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

To avoid issues with [image resizing](https://docs.anthropic.com/en/docs/build-with-claude/vision#evaluate-image-size), it's recommended to not send screenshots with resolutions higher than [XGA/WXGA](https://en.wikipedia.org/wiki/Display_resolution_standards#XGA). Relying on the API's image resizing behavior results in lower model accuracy and slower performance compared to implementing scaling directly in the tool.  The `computer` tool implementation in this project demonstrates how to scale images and coordinates from higher resolutions down to the recommended resolution.

## Development

```bash
./setup.sh  # Sets up venv, installs development dependencies, and installs pre-commit hooks
docker build . -t computer-use-demo:local  # Manually build Docker image (optional)
export ANTHROPIC_API_KEY=%your_api_key%
docker run \
    -e ANTHROPIC_API_KEY=$ANTHROPIC_API_KEY \
    -v $(pwd)/computer_use_demo:/home/computeruse/computer_use_demo/ # Mounts local Python modules for development \
    -v $HOME/.anthropic:/home/computeruse/.anthropic \
    -p 5900:5900 \
    -p 8501:8501 \
    -p 6080:6080 \
    -p 8080:8080 \
    -it computer-use-demo:local  # You can also use ghcr.io/anthropics/anthropic-quickstarts:computer-use-demo-latest
```

The above `docker run` command mounts the repository inside the Docker image so that you can edit it from your host. Streamlit auto-reload is already configured.