import telebot
from dotenv import load_dotenv


load_dotenv()

my_secret = os.environ['API_KEY']
bot = telebot.TeleBot(my_secret)
