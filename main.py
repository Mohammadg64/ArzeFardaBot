import os
import telebot

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "به ربات سیگنال‌دهی ArzeFarda خوش آمدید!")

@bot.message_handler(commands=["signal"])
def send_signal(message):
    bot.reply_to(message, "سیگنال تست: خرید BTC در 58000 با هدف 61000 و حد ضرر 57000")

bot.polling()