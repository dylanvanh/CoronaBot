import os
from test import photo
from numpy import split
import telebot
from dotenv import load_dotenv
import pandas as pd
import matplotlib.pyplot as plt
# from datetime import datetime ,date


load_dotenv()

my_secret = os.environ['API_KEY']
bot = telebot.TeleBot(my_secret)

DATA = 'https://covid.ourworldindata.org/data/owid-covid-data.csv' #download the csv file 