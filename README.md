# Telegram AI Chat Bot

A simple Telegram bot that uses Google's Gemini AI model to respond to user messages. The bot processes any text message sent to it and returns AI-generated responses.

## Features

- Responds to `/start` and `/help` commands with an introduction message
- Processes any text message using Google's Gemini AI model
- Simple error handling for API failures

## Prerequisites

- Python 3.9 or higher
- A Telegram Bot Token (from [@BotFather](https://t.me/botfather))
- A Google Gemini API Key (from [Google AI Studio](https://makersuite.google.com/app/apikey))

## Installation

1. Clone this repository:
```bash
git clone https://github.com/thisisisheanesu/telegram-llm-bot
cd telegram-llm-bot
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with your API keys:
```
TELEGRAM_API_KEY=your_telegram_bot_token
GEMINI_API_KEY=your_gemini_api_key
```

## Running the Bot

1. Make sure your `.env` file is properly configured with valid API keys
2. Run the bot:
```bash
python bot.py
```

3. Start chatting with your bot on Telegram!

## Usage

1. Start a chat with your bot on Telegram
2. Send `/start` or `/help` to get the introduction message
3. Send any message to get an AI-generated response

## License

[MIT License](LICENSE)
