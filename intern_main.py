import os
import telebot 
import numpy as np
import pandas as pd
import database

API_KEY = '5220149302:AAGvHi-tjaBaAwlTsmLVGFaBiicNcX8G1a0'
bot = telebot.TeleBot(API_KEY)

pkmndata = pd.read_csv(r"C:\Users\Zhi Yang\OneDrive\Documents\NTU y1s2 mods\Hackathon\internship_test.csv")
hi = pkmndata.head()
print(hi)

 



@bot.message_handler(commands=['getvalues'])
def greet(update):

    #def send_download(update):
    message_text = update.message.text
    todo_title = message_text.replace("/command ", "")
    pkmndata = pd.read_csv(r"C:\Users\Zhi Yang\OneDrive\Documents\NTU y1s2 mods\Hackathon\internship_test.csv")
    code_html='*{}*.'.format(todo_title)  
    if pkmndata.empty == False:
        for i in range(5):
            code_html=code_html + '\n\n {}:'.format(todo_title) + str((pkmndata[todo_title].iloc[i]))
    bot.send_message(message.chat.id, code_html)
    
@bot.message_handler(commands=['start'])
def start(message):
    text = "Hi this is a internship search portal chat bot. Feel free to use it! If you need help, feel free to use /help command."
    bot.send_message(message.chat.id, text)



def send_download(update):
    message_text = update.effective_message.text
    todo_title = message_text.replace("/command ", "")



@bot.message_handler(commands=['columns'])
def columns(message):
    st = ""
    data_header = ['Index', 'image', 'company', 'city', 'state', 'year', 'Season',
       'monthlySalary', 'language', 'benefits', 'applyLink']
    for header in data_header:
        st += header
        st += '\n'
    bot.send_message(message.chat.id, st)




    

@bot.message_handler(commands=['getValues'])

def exchange_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(telebot.types.InlineKeyboardButton('Id', callback_data='get-Id'))
    keyboard.row(telebot.types.InlineKeyboardButton('Next', callback_data='get-Id'),telebot.types.InlineKeyboardButton('MSZoning', callback_data='get-MSZoning'))
    bot.send_message(message.chat.id, 'Click on the column you want:', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
   data = query.data
   if data.startswith('get-'):
       get_ex_callback(query)

def get_ex_callback(query):
   bot.answer_callback_query(query.id)
   send_exchange_result(query.message, query.data[4:])


def send_exchange_result(message, ex_code):
   cnt = 0
   bot.send_chat_action(message.chat.id, 'typing')
   ex, cnt = database.get_values(ex_code, cnt)
   keyboard = telebot.types.InlineKeyboardMarkup()
   keyboard.row(telebot.types.InlineKeyboardButton('Id', callback_data='get-Id'))
   bot.send_message(
       message.chat.id, ex
   )


@bot.message_handler(commands=['salary'])
def compute_salary(message):
    ex = 'HI'
    bot.send_message(message.chat.id, ex)
            


   

@bot.message_handler(commands=['help'])
def help_command(message):
   keyboard = telebot.types.InlineKeyboardMarkup()
   keyboard.add(
       telebot.types.InlineKeyboardButton(
           "Message the developer", url='telegram.me/yinjiann'
       )
   )
   bot.send_message(
       message.chat.id,
       '1) <year: \U0001F4C6, season: \U0001F343>: year and season should not be case-sensitive.\n     Season: Winter, Summer, Fall, Spring\n' +
       '2) <company name: \U0001F3E2>: name must be case-sensitive\n' +
       '3) <city name: \U0001F4CD>: name must be case-sensitive.\n',
       reply_markup=keyboard
   )

# allows user to retrieve col values based on input values
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    message_text = message.text
    #bot.reply_to(message, message_text)

    data_header = ['Index', 'image', 'company', 'city', 'season', 'year',
       'monthlySalary', 'benefits', 'applyLink']

    ls = message_text.split()
    # if message_text do not ask for salary, just for column values, you will return the first 5 values under the specified column
    if message_text in data_header:
        ex = database.get_values(message_text)
        bot.send_message(message.chat.id, ex)
    # else if message_text ask for salary, you will return first 5 salaries that is below the inputted values and the first 5 salaries that is above the inputted values
    elif 'salary' in ls:
        for element in ls:
            if element.isdigit():
                amount = int(element)
                ex = database.get_salary(amount)
                if ex == "":
                    reply = "Sorry no internships available in {}".format(amount)
                    bot.send_message(message.chat.id, reply)
                else:
                    bot.send_message(message.chat.id, ex)
        
    # else if message_text ask for specific year and season, it will return the first 5 entries
    elif "year" in message_text:
        s = message_text.split(" ")
        
        if (s[-2].isdigit() and s[-1].capitalize() in ['Summer', 'Winter', 'Fall', 'Spring']):
            ex = database.hiring_season(int(s[-2]), s[-1].capitalize())
            if ex == "":
                reply = "Sorry no internships available in {}".format(s[-1])
                bot.send_message(message.chat.id, reply)
            else:
                bot.send_message(message.chat.id, ex)
            
        else:
            ex = 'fk u u noe'
            bot.send_message(message.chat.id, ex)
            
    elif "city" in message_text:
        s = message_text.split(" ", 1)
        ex = database.find_cities(s[-1].capitalize())
        if (ex == ""):
            reply = "Sorry no internships available in {}".format(s[-1])
            bot.send_message(message.chat.id, reply)
        else:
            bot.send_message(message.chat.id, ex)

    elif "company" in message_text:
        s = message_text
        ex = database.get_company(s[8:])
        if (ex == ""):
            reply = "Sorry no internships available in {}".format(s[8:])
            bot.send_message(message.chat.id, reply)
        else:
            bot.send_message(message.chat.id, ex)

            
    else:
        ex = "Sorry not available in data"
        bot.send_message(message.chat.id, ex)


  
bot.polling()

