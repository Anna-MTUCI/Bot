import telebot
from telebot import types
import psycopg2
import datetime
from datetime import datetime

bot=telebot.TeleBot('2134927259:AAHW-JORj8bDZIZ_VIsNAGF_svD1g8hk1V0')

def clav_message():
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Расписание пар по дням неделям')
    btn12 = types.KeyboardButton('Расписание на сегодня')
    btn13 = types.KeyboardButton('Расписание на завтра')
    markup.add(btn1)
    markup.add(btn12)
    markup.add(btn13)
    return markup

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Привет я помогу тебе ориентороваться в моем боте. 1. Базовые команды бота: \n/start-начать работу бота \n/help-командный помощник \n/button- вызов кнопки бота')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, вызови команду /button чтобы продолжить работу с ботом')

@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Расписание пар по дням неделям')
    btn12 = types.KeyboardButton('Расписание на сегодня')
    btn13 = types.KeyboardButton('Расписание на завтра')
    markup.add(btn1)
    markup.add(btn12)
    markup.add(btn13)
    bot.send_message(message.chat.id, 'На когда вам нужно расписание?', reply_markup=markup)

@bot.message_handler(content_types='text')
def reply_message(message):
    if message.text == 'Расписание пар по дням неделям':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn2 = types.KeyboardButton('Понедельник')
        btn3 = types.KeyboardButton('Вторник')
        btn4 = types.KeyboardButton('Среда')
        btn5 = types.KeyboardButton('Четверг')
        btn6 = types.KeyboardButton('Пятница')
        btn7 = types.KeyboardButton('Суббота')
        markup.add(btn2)
        markup.add(btn3)
        markup.add(btn4)
        markup.add(btn5)
        markup.add(btn6)
        markup.add(btn7)

        
        bot.send_message(message.chat.id, 'На какой день недели нужно расписание', reply_markup=markup)
        
    if message.text == 'Понедельник':
        coon=psycopg2.connect(database="postgres",user="postgres",password="Anna25",host="localhost",port="5432")
        cursor=coon.cursor()
        cursor.execute("SELECT day, subject,room_numb, start_time FROM timetable WHERE day='понедельник'")
        records=cursor.fetchall()
        result=''
        for arr in records:
            for word in arr:
                result+=str(word)
                result+='\n'
        bot.send_message(message.chat.id, result, reply_markup=clav_message())
          
    if message.text == 'Вторник':
        coon=psycopg2.connect(database="postgres",user="postgres",password="Anna25",host="localhost",port="5432")
        cursor=coon.cursor()
        cursor.execute("SELECT day, subject,room_numb, start_time FROM timetable WHERE day='вторник'")
        records=cursor.fetchall()
        result=''
        for arr in records:
            for word in arr:
                result+=str(word)
                result+='\n'
        bot.send_message(message.chat.id, result, reply_markup=clav_message())
         
    if message.text == 'Среда':
        coon=psycopg2.connect(database="postgres",user="postgres",password="Anna25",host="localhost",port="5432")
        cursor=coon.cursor()
        cursor.execute("SELECT day,subject,room_numb, start_time FROM timetable WHERE day='среда'")
        records=cursor.fetchall()
        result=''
        for arr in records:
            for word in arr:
                result+=str(word)
                result+='\n'
        bot.send_message(message.chat.id, result, reply_markup=clav_message())
    if message.text == 'Четверг':
        coon=psycopg2.connect(database="postgres",user="postgres",password="Anna25",host="localhost",port="5432")
        cursor=coon.cursor()
        cursor.execute("SELECT day, subject,room_numb, start_time FROM timetable WHERE day='четверг'")
        records=cursor.fetchall()
        result=''
        for arr in records:
            for word in arr:
                result+=str(word)
                result+='\n'
        bot.send_message(message.chat.id, result, reply_markup=clav_message())  
    if message.text == 'Пятница':
        coon=psycopg2.connect(database="postgres",user="postgres",password="Anna25",host="localhost",port="5432")
        cursor=coon.cursor()
        cursor.execute("SELECT day, subject,room_numb, start_time FROM timetable WHERE day='пятница'")
        records=cursor.fetchall()
        result=''
        for arr in records:
            for word in arr:
                result+=str(word)
                result+='\n'
        bot.send_message(message.chat.id, result, reply_markup=clav_message())

    if message.text == 'Суббота':
        coon=psycopg2.connect(database="postgres",user="postgres",password="Anna25",host="localhost",port="5432")
        cursor=coon.cursor()
        cursor.execute("SELECT day, subject,room_numb, start_time FROM timetable WHERE day='суббота'")
        records=cursor.fetchall()
        result=''
        for arr in records:
            for word in arr:
                result+=str(word)
                result+='\n'
        bot.send_message(message.chat.id, result, reply_markup=clav_message())
    

    if message.text == 'Расписание на сегодня':
        today=datetime.today().weekday()
        if today==6:
            bot.send_message(message.chat.id, 'Выходной')
        else:
            bot.send_message(message.chat.id, today)
            days= ['понедельник','вторник','среда','четверг','пятница','суббота','воскресенье']
            ceg=str(days[today])
            bot.send_message(message.chat.id, ceg)
            coon=psycopg2.connect(database="postgres",user="postgres",password="Anna25",host="localhost",port="5432")
            cursor=coon.cursor()
            cursor.execute("SELECT day, subject,room_numb, start_time FROM timetable WHERE day=%s",[ceg])
            records=cursor.fetchall()
            result=''
            for arr in records:
                for word in arr:
                    result+=str(word)
                    result+='\n'
            bot.send_message(message.chat.id, result) 
            
    if message.text == 'Расписание на завтра':
        today=datetime.today().weekday()+1
        bot.send_message(message.chat.id, today)
        if today==7:
            today=0
        days= ['понедельник','вторник','среда','четверг','пятница','суббота','воскресенье']
        ceg=str(days[today])
        bot.send_message(message.chat.id, ceg)
        coon=psycopg2.connect(database="postgres",user="postgres",password="Anna25",host="localhost",port="5432")
        cursor=coon.cursor()
        cursor.execute("SELECT day, subject,room_numb, start_time FROM timetable WHERE day=%s",[ceg])
        records=cursor.fetchall()
        result=''
        for arr in records:
            for word in arr:
                result+=str(word)
                result+='\n'
        bot.send_message(message.chat.id, result) 
        

bot.infinity_polling()