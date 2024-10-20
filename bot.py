import telebot

botTimeWeb = telebot.TeleBot('7775731838:AAG2TUJLBlTQsqno4TLZ1OBOoqFOQ5PyYcY')

from telebot import types

@botTimeWeb.message_handler(commands=['start'])
def startBot(message):
  first_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, hi!\n, would you like to tell me about myself?"
  markup = types.InlineKeyboardMarkup()
  button_yes = types.InlineKeyboardButton(text = 'Yes', callback_data='yes')
  markup.add(button_yes)
  botTimeWeb.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)
@botTimeWeb.callback_query_handler(func=lambda call:True)
def response(function_call):
  if function_call.message:
     if function_call.data == "yes":
        second_mess = "I am a programmer who develops telegram bots, you can see my work on my website!"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Go to site", url="https://github.com/ValeriiKleshnia"))
        botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
        botTimeWeb.answer_callback_query(function_call.id)
botTimeWeb.infinity_polling()
