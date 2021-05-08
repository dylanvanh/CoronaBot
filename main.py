import os
import telebot
from dotenv import load_dotenv
import pandas as pd
# from matplotlib.pyplot import plt 
# from datetime import datetime ,date

# from covid import Covid



load_dotenv()

my_secret = os.environ['API_KEY']
bot = telebot.TeleBot(my_secret)

# DATA = 'https://covid.ourworldindata.org/data/owid-covid-data.csv' #download the csv file 

#/start replies
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Type /help for commands")

#/help , replies
@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message,'Type /showstats (country name) - to show latest stats\n'+
                        'Type /graph (countryname) - for a full graph of a countries cases'
                        )

##sends back every message sent , only runs when another command isnt called
# @bot.message_handler(func = lambda message :True)
# def get_country(message):
#     bot.reply_to(message,message.text)


#checking message from chat
@bot.message_handler(content_types=['text'])
def send_text(message):
    print(message.text)
    if message.text == 'test':
        bot.send_message(message.chat.id,'text was test')

    if message.text == 'boet':
        bot.send_message(message.chat.id,'boet was test')

#replies if a message is a sticker
@bot.message_handler(content_types=['sticker'])
def test(message):
    bot.send_message(message,'sticker boss')



bot.polling()





































#     country = message.text
#     df = pd.read_csv(DATA) #read the csv file
#     df['date'] = pd.to_datetime(df.date) #convert the data
#     df.fillna(0)

#     za = df[df['location'] == 'South Africa'] # '{country} , user inputted country stats are shown , get input from user
#     latest_info = za.iloc[-1] #last day in the dataset
#     previous_day = za.iloc[-2] #2nd last day in the dataset

#     '''
#     2 - Location
#     3 - Date`
#     4 - total cases
#     5 - new cases
#     6 - total deaths
#     7 - new deaths
#     34- total vaccinations
#     37 - new vaccinations
#     '''
#     # output = 'country = {}'.format(country)
#     output = 'Location = {}\nDate = {}\nNew Cases = {}\nNew Deaths = {}\nNew Vaccinations = {}\nTotal Cases = {}\nTotal Deaths = {}\nTotal Vaccinations = {}\
#         '.format(country,latest_info[3].strftime('%Y-%m-%d'),latest_info[5].astype(str),
#                 latest_info[7].astype(str),latest_info[37].astype(str),latest_info[4].astype(str),``
#                 latest_info[6].astype(str),latest_info[34].astype(str))
#     bot.send_message(message.chat.id,output)



# data = 'https://covid.ourworldindata.org/data/owid-covid-data.csv' #the covid data
# df = pd.read_csv(data) #read the csv file
# df['date'] = pd.to_datetime(df.date) #convert the data
# df.fillna(0)



# za = df[df['location'] == 'South Africa'] 


# #graph
# def create_graph():
#     fig , ax = plt.subplots(figsize=(12,6))
#     ax.ticklabel_format(style='plain')
#     ax.plot(za.date,za.new_cases_smoothed,'b')
#     ax.set_title('New Cases in {country}')
#     ax.set_ylabel('Amount of Cases')
#     ax.set_xlabel('Date')
#     ax.legend(['New Cases'])
#     from datetime import datetime,timedelta #program kept forgetting import just doing incase
#     date = datetime.now()
#     date = str(date)
#     date = date.strip()
#     date = date.replace(':','-')
#     plt.savefig('covid_graph'+date+'.png') #saves file
#     return 'covid_graph'+date+'.png' #filename

'''
get the df for covid world
use pandas to thingy it for za
show last entry on thing, new cases and total cases
maybe allow input for searching the whole world by country name?
'''



