# import everything
from flask import Flask
import telegram
from telegram.ext import Dispatcher
from flasktele.secret import bot_token, bot_username, heroku_url
from flask_sqlalchemy import SQLAlchemy

global TOKEN
global bot

TOKEN = bot_token

bot = telegram.Bot(token=TOKEN)
dispatcher = Dispatcher(bot, None, use_context=True)


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from flasktele import linkurl
