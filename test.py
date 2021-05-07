import os
import telebot
from dotenv import load_dotenv
import pandas as pd


load_dotenv()

my_secret = os.environ['API_KEY']
bot = telebot.TeleBot(my_secret)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Type /help to see commands")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message,'Type /showstats to show the previous days stats for South Africa')



bot.polling()