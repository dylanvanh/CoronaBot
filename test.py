
import matplotlib.pyplot as plt
import pandas as pd

DATA = 'https://covid.ourworldindata.org/data/owid-covid-data.csv' #download the csv file 


df = pd.read_csv(DATA) #read the csv file
df['date'] = pd.to_datetime(df.date) #convert the data
df.fillna(0)




#graph
def create_graph(country):

    country_df = df[df['location'] == 'South Africa']
    fig , ax = plt.subplots(figsize=(12,6))
    ax.ticklabel_format(style='plain')
    ax.plot(country_df.date,country_df.new_cases_smoothed,'b')
    ax.set_title('New Cases in',country)
    ax.set_ylabel('Amount of Cases')
    ax.set_xlabel('Date')
    ax.legend(['New Cases'])

    from datetime import datetime #program kept forgetting import just doing incase

    # date = datetime.now()
    # date = str(date)
    # date = date.strip()
    # date = date.replace(':','-')
    plt.savefig('covid_graph.png') #saves file
    return 'covid_graph.png' #filename




def create_graph(country):
    country_df = df[df['location'] == country]
    fig , ax = plt.subplots(figsize=(12,6))
    ax.ticklabel_format(style='plain')

    ax.plot(country_df.date,country_df.new_cases_smoothed,'b')

    ax.set_title('New Cases in South Africa')
    ax.set_ylabel('Amount of Cases')
    ax.set_xlabel('Date')
    ax.legend(['New Cases'])

    from datetime import datetime,timedelta #program kept forgetting import just doing incase
    date = datetime.now()
    date = str(date)
    date = date.strip()
    date = date.replace(':','-')
    plt.savefig('covid_graph'+date+'.png') #saves file
    return 'covid_graph.png' #filename

print(create_graph('South Africa'))
