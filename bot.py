from dotenv import load_dotenv
import os
import telebot

# Load environment variables from .env file
load_dotenv()

from providers.gemini import call_gemini_api

# Telegram init
telegram_api_key = os.getenv('TELEGRAM_API_KEY')
bot = telebot.TeleBot(telegram_api_key)

# /start and /help' commands
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
	bot.reply_to(message, "Ask me anything and I'll do my best to answer you! This is a demo bot that uses an LLM to answer your questions.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
	response = call_gemini_api(message.text)
	bot.reply_to(message, response)

# Start bot
bot.infinity_polling()
