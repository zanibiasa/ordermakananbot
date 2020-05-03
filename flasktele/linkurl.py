from flasktele import app, TOKEN, heroku_url, bot, db, dispatcher
from telegram.ext import MessageHandler, Filters, Dispatcher, CommandHandler, CallbackQueryHandler
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from flask import request
from flasktele.mastermind import get_response
from flasktele.pengkalandata import User
#import flasktele.semuasenarai as manue
from flasktele.semuasenarai import array_senarai, list_keyboardbutton



def handler_start(update, context):
    

    update.message.reply_text(main_menu_message(update),
                            reply_markup=main_menu_keyboard())
  #  bot.sendMessage(chat_id=update.message.chat_id, text=text)

def handler_membeli(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
                            text=menu_senaraikedai_message(),
                            reply_markup=menu_senaraikedia_keyboard())

def main_menu_message(update):
    nama = update.message.from_user['first_name']
   
    return f'Hi {nama}, Kau nak apa? '

def menu_senaraikedai_message():
    return 'Nak kedai mana'
  
def main_menu_keyboard():
    
    return InlineKeyboardMarkup(list_keyboardbutton)


    

def menu_senaraikedia_keyboard():
    keyboard = [[InlineKeyboardButton('speedmart', callback_data='handler_membeli')],
                [InlineKeyboardButton('2ya', callback_data='m2')],
                [InlineKeyboardButton('mee celup', callback_data='m2')],
                [InlineKeyboardButton("zack n' mart", callback_data='m2')],
                ]
    return InlineKeyboardMarkup(keyboard)


dispatcher.add_handler(CommandHandler('start', handler_start))
#dispatcher.add_handler(MessageHandler(Filters.text, handler_nama))
dispatcher.add_handler(CallbackQueryHandler(handler_membeli, pattern='handler_membeli'))





@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    #updatetry = request.get_json(force=True)
   # print(updatetry)
    # retrieve the message in JSON and then transform it to Telegram object
    update = Update.de_json(request.get_json(force=True), bot)
    print(update)
    #baca =update.message.text.encode('utf-8').decode()
# get the chat_id to be able to respond to the same user
    dispatcher.process_update(update)

    
   # print(baca)
    return 'ok'
   # chat_id = update.message.chat.id
  #  msg_id = update.message.message_id
  #  text = update.message.text.encode('utf-8').decode()
   # user = User(username= chat_id, nama=text)
  #  db.session.add(user)
  #  db.session.commit()
    # get the message id to be able to reply to this specific message
  #  msg_id = update.message.message_id
# Telegram understands UTF-8, so encode text for unicode compatibility
  #  text = update.message.text.encode('utf-8').decode()
  #  print("got text message :", text)
# here we call our super AI
  #  response = get_response(text)
# now just send the message back
    # notice how we specify the chat and the msg we reply to
   # bot.sendMessage(chat_id=chat_id, text=response, reply_to_message_id=msg_id)
   # return 'ok'


@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    # we use the bot object to link the bot to our app which live
    # in the link provided by URL
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=heroku_url, HOOK=TOKEN))
    # something to let us know things work
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"

# @app.route('/')
# def index():
#     return '.'

@app.route('/testingje')
def testingje():
    array_senarai()
    
    return '.'