# DlightAI Chatbot Documentation

## Overview
DlightAI is a state-of-the-art chatbot powered by the Kimi-K2.5 model. This document serves as comprehensive documentation covering setup, usage, features, and deployment to Hugging Face Spaces.

## Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/develight1-cloud/dlight-ai-chatbot.git
   cd dlight-ai-chatbot
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.8+ installed. You can set up a virtual environment and install the required packages:
   ```bash
   python -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```

3. **Configuration**:
   Update the configuration file as needed. Refer to `config.yaml` for more details.

## Usage
1. **Running the Chatbot**:
   You can run the DlightAI chatbot using:
   ```bash
   python app.py
   ```
   By default, it will start on `http://localhost:5000`.

2. **Interacting with the Chatbot**:
   Use CURL, Postman, or any HTTP client to send requests to the chatbot.
   ```bash
   curl -X POST http://localhost:5000/chat -H "Content-Type: application/json" -d '{"message":"Hello!"}'
   ```

## Features
- **AI-Powered Conversations**: Leverages Kimi-K2.5 for intelligent responses.
- **Multi-turn Conversations**: Supports ongoing dialogues for a more natural interaction.
- **Customizable Responses**: Easily customize responses through the configuration file.

## Deployment to Hugging Face Spaces
To deploy the DlightAI chatbot to Hugging Face Spaces, follow these steps:
1. **Create a new Space** on Hugging Face with the appropriate environment (e.g., Gradio).
2. **Push your code** to the newly created Space. Use the following command:
   ```bash
   git push https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME
   ```
3. **Test your deployment** on Hugging Face Spaces, ensuring that everything is functioning as expected.

## Conclusion
DlightAI provides a robust solution for developing interactive chatbots using the Kimi-K2.5 model. With easy setup and deployment, you can create fantastic conversational experiences.