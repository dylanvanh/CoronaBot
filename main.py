import os
import telebot
from dotenv import load_dotenv
import pandas as pd
from matplotlib.pyplot import plt 
from datetime import datetime ,date

# from covid import Covid



load_dotenv()

my_secret = os.environ['API_KEY']
bot = telebot.TeleBot(my_secret)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Type /help to see commands")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message,'Type /showstats to show the previous days stats for South Africa')


country = ''

data = 'https://covid.ourworldindata.org/data/owid-covid-data.csv' #the covid data
df = pd.read_csv(data) #read the csv file
df['date'] = pd.to_datetime(df.date) #convert the data
df.fillna(0)



za = df[df['location'] == 'South Africa'] # if question is for South Africa


#graph
def create_graph():
    fig , ax = plt.subplots(figsize=(12,6))
    ax.ticklabel_format(style='plain')
    ax.plot(za.date,za.new_cases_smoothed,'b')
    ax.set_title('New Cases in {country}')
    ax.set_ylabel('Amount of Cases')
    ax.set_xlabel('Date')
    ax.legend(['New Cases'])
    from datetime import datetime,timedelta #program kept forgetting import just doing incase
    date = datetime.now()
    date = str(date)
    date = date.strip()
    date = date.replace(':','-')
    plt.savefig('covid_graph'+date+'.png') #saves file
    return 'covid_graph'+date+'.png' #filename

'''
get the df for covid world
use pandas to thingy it for za
show last entry on thing, new cases and total cases
maybe allow input for searching the whole world by country name?
'''



bot.polling()