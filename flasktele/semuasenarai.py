from flasktele.linkurl import Update
from flasktele.pengkalandata import User, Makanan
from telegram import InlineKeyboardButton

list_keyboardbutton = [[InlineKeyboardButton('speedmart', callback_data='handler_membeli')]]

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
    keyboard = [[InlineKeyboardButton('Membeli', callback_data='handler_membeli')],
              [InlineKeyboardButton('Menjual', callback_data='m2')],
              ]
    return InlineKeyboardMarkup(keyboard)

def menu_senaraikedia_keyboard():
    keyboard = [[InlineKeyboardButton('speedmart', callback_data='handler_membeli')],
                [InlineKeyboardButton('2ya', callback_data='m2')],
                [InlineKeyboardButton('mee celup', callback_data='m2')],
                [InlineKeyboardButton("zack n' mart", callback_data='m2')],
                ]
    return InlineKeyboardMarkup(keyboard)



def array_senarai():
    list_keyboardbutton = []
    total_senarai = User.query.all()
    

    for total in total_senarai:
        username = str(total.username)
        nama = str(total.nama)
        keyboardbutton = [InlineKeyboardButton(nama, callback_data=username)]
        list_keyboardbutton.append(keyboardbutton)

def array_senarai_makanan(username_kedai):

    total_senarai_makanan = Makanan.query.filter_by(kedai.username==username_kedai).all()
    for a in total_senarai_makanan:
        usernamnamamakanan = str(a.namamakanan)
        #nama = str(a.)
        keyboardbutton = [InlineKeyboardButton(nama, callback_data=username)]
        list_keyboardbutton.append(keyboardbutton)
