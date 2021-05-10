import os
import telebot
from dotenv import load_dotenv
import pandas as pd
import matplotlib.pyplot as plt
# from datetime import datetime ,date


load_dotenv()

my_secret = os.environ['API_KEY']
bot = telebot.TeleBot(my_secret)

DATA = 'https://covid.ourworldindata.org/data/owid-covid-data.csv' #download the csv file 

#/start replies
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Type /help for commands")

#/help , replies
@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message,'stats (country name) - (e.g. stats China)\n'+
                        'graph (country name) - (e.g graph China)')

#graph
def create_graph(country):

    country_df = load_dataset(country)

    if country_df.empty:
        return 'Country : ' + str(country) +" doesnt exist",False

    fig , ax = plt.subplots(figsize=(12,6))
    ax.ticklabel_format(style='plain')

    ax.plot(country_df.date,country_df.new_cases_smoothed,'b')

    ax.set_title('New Cases in ' + str(country))
    ax.set_ylabel('Number of Cases')
    ax.set_xlabel('Date')
    ax.legend(['New Cases'])

    from datetime import datetime #program kept forgetting import just doing incase
    date = datetime.now()
    date = str(date)
    date = date.strip()
    date = date.replace(':','-')
    plt.savefig('covid_graph'+date+'.png') #saves file

    return 'covid_graph'+date+'.png',True #filename


def format_input(user_message):
    split_message = user_message.lower().title().split()
    output = ''

    for i in range(len(split_message)):
        if i != 0:
            output += split_message[i] + ' '
    country_name = output.strip()

    return split_message,country_name

def country_acronym(country):
    #converts a few of the long named countries into acronyms
    if country.lower() == 'za':
        return 'South Africa'
    
    if country.lower() == 'usa':
        return 'United States'
    
    if country.lower() == 'uk':
        return 'United Kingdom'

    if country.lower() == 'drc':
        return 'Democratic Republic of Congo'

    if country.lower() == 'na':
        return 'North America'
    
    if country.lower() == 'sa':
        return 'South America'

    return country    


def load_dataset(country):
    df = pd.read_csv(DATA) #read the csv file
    df['date'] = pd.to_datetime(df.date) #convert the data
    df.fillna(0)
    country = country_acronym(country)
    country_df = df[df['location'] == country]

    return country_df

@bot.message_handler(content_types=['text'])
def get_stats(message):

    split_message,country_name = format_input(message.text)

    if split_message[0].lower() == 'graph':

        bot.reply_to(message,'graph processing')
        
        country_name = country_acronym(country_name)

        photo_name,passed_check = create_graph(country_name)

        if passed_check:
            print('photoname = ' + str(photo_name))
            bot.reply_to(message,photo_name)
            photo = open(photo_name, 'rb')
            bot.send_photo(message.chat.id,photo)
            os.remove(photo_name)
        else:
            bot.reply_to(message,'Invalid Country Name')



    if split_message[0].lower() == 'stats':
        bot.reply_to(message,'Stats processing')
        try:

            country_df = load_dataset(country_name)

            latest_info = country_df.iloc[-1] #last day in the dataset


            #location,latest_Date,new_cases,new_deaths,new_vaccinations,total_cases,total_deaths,total_vacciantions
            output = 'Location = {}\nLatest Date = {}\nNew Cases = {}\nNew Deaths = {}\nNew Vaccinations = {}\nTotal Cases = {}\nTotal Deaths = {}\nTotal Vaccinations = {}\
                '.format(country_name,latest_info[3].strftime('%Y-%m-%d'),latest_info[5].astype(str),
                latest_info[8].astype(str),latest_info[37].astype(str),latest_info[4].astype(str),
                latest_info[7].astype(str),latest_info[34].astype(str))
            
            bot.send_message(message.chat.id,output)

        except:
            bot.reply_to(message,'Invalid Country Name')

        

#replies if a message is a sticker
@bot.message_handler(content_types=['sticker'])
def test(message):
    bot.send_message(message,'sticker boss')



bot.infinity_polling()

'''
get the df for covid world
use pandas to thingy it for za
show last entry on thing, new cases and total cases
maybe allow input for searching the whole world by country name?
'''



