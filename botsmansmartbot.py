import pyowm
import telebot
from telebot import types
import requests

owm = pyowm.OWM('55654dc1b5773bafd24ba70ab0b40ee4', language="ru")
bot = telebot.TeleBot("929266762:AAGMsHo5fflXm4YmCFJVdTWVNGcGtEYGgdM")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    command = message.text

    def show_menu():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        itembtn1 = types.KeyboardButton('Погода')
        itembtn2 = types.KeyboardButton('Прогноз погоды')
        itembtn3 = types.KeyboardButton('Ыч')
        itembtn4 = types.KeyboardButton('Курс валют')
        itembtn5 = types.KeyboardButton('Скрыть')
        itembtn6 = types.KeyboardButton('Закрыть')
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
        markup.row(itembtn5, itembtn6)
        bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)
        #markup()
    def hide_menu():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        itembtn11 = types.KeyboardButton('Ыч')
        itembtn12 = types.KeyboardButton('Закрыть')
        markup.add(itembtn11, itembtn12)
        bot.send_message(message.chat.id, "hide", reply_markup=markup)
    def close_menu():
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, 'Ok', reply_markup=markup)

    
    if "Погода" in command or "погода" in command:
        observation = owm.weather_at_place( 'Kyiv' )
        w=observation.get_weather()
        temp = w.get_temperature('celsius')["temp"]

        answer="В городе Киев сейчас "+w.get_detailed_status()+ "\n"
        answer+="Температура около "+ str(temp)+"\n\n"
        if temp < 0:
            answer += "Зима на улице, сиди дома"
        elif temp < 10:
                answer += "Холодно шо писец, шубу одевай"
        elif temp < 20:
            answer += "Прохладно, оденься"
        else:
            answer += "Нормас погода"

        bot.send_message(message.chat.id, answer)
        
    elif "Прогноз погод" in command or "прогноз погод" in command:
        fc = owm.three_hours_forecast( 'Kyiv' )
        f = fc.get_forecast()
        answer=""
        t1min=t2min=t3min=t4min=t5min=t6min=+100
        t1max=t2max=t3max=t4max=t5max=t6max=-100
        day1=day2=day3=day4=day5=day6=0
        mnt1=mnt2=mnt3=mnt4=mnt5=mnt6=0
        
        for weather in f: 
            d=weather.get_reference_time(timeformat='date')
            if day1 == 0 or day1 == d.day:
                day1 = d.day
                mnt1 = d.strftime("%B")
                t1min=min(t1min,weather.get_temperature('celsius')["temp_min"])
                t1max=max(t1max,weather.get_temperature('celsius')["temp_max"])
            elif day2 == 0 or day2 == d.day:
                day2 = d.day
                mnt2 = d.strftime("%B")
                t2min=min(t2min,weather.get_temperature('celsius')["temp_min"])
                t2max=max(t2max,weather.get_temperature('celsius')["temp_max"])
            elif day3 == 0 or day3 == d.day:
                day3 = d.day
                mnt3 = d.strftime("%B")
                t3min=min(t3min,weather.get_temperature('celsius')["temp_min"])
                t3max=max(t3max,weather.get_temperature('celsius')["temp_max"])
            elif day4 == 0 or day4 == d.day:
                day4 = d.day
                mnt4 = d.strftime("%B")
                t4min=min(t4min,weather.get_temperature('celsius')["temp_min"])
                t4max=max(t4max,weather.get_temperature('celsius')["temp_max"])
            elif day5 == 0 or day5 == d.day:
                day5 = d.day
                mnt5 = d.strftime("%B")
                t5min=min(t5min,weather.get_temperature('celsius')["temp_min"])
                t5max=max(t5max,weather.get_temperature('celsius')["temp_max"])
            elif day6 == 0 or day6 == d.day:
                day6 = d.day
                mnt6 = d.strftime("%B")
                t6min=min(t6min,weather.get_temperature('celsius')["temp_min"])
                t6max=max(t6max,weather.get_temperature('celsius')["temp_max"])
 
        answer += (str(day1) + " , " + str(mnt1) + " : " + str(t1min) + " °C ... " + str(t1max) + " °C;" + "\n")
        answer += (str(day2) + " , " + str(mnt2) + " : " + str(t2min) + " °C ... " + str(t2max) + " °C;" + "\n")
        answer += (str(day3) + " , " + str(mnt3) + " : " + str(t3min) + " °C ... " + str(t3max) + " °C;" + "\n")
        answer += (str(day4) + " , " + str(mnt4) + " : " + str(t4min) + " °C ... " + str(t4max) + " °C;" + "\n")
        answer += (str(day5) + " , " + str(mnt5) + " : " + str(t5min) + " °C ... " + str(t5max) + " °C;" + "\n")
        if day6!=0:
            answer += (str(day6) + " , " + str(mnt6) + " : " + str(t6min) + " °C ... " + str(t6max) + " °C;" + "\n")

        bot.send_message(message.chat.id, answer)
	
    elif message.text == 'Курс валют' or message.text == 'курс валют' or message.text == '/Курс валют' or message.text == '/курс валют':

        ldata = requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5").json()
        answer = '`/     Покупка   Продажа`' + '\n'
        data = [ldata[0],ldata[1],ldata[2]]
        for kl in data:
 
            strg = ((kl['ccy']+kl['buy'][:-2].rjust(10,"_")+kl['sale'][:-2].rjust(10,"_")))
 
            answer += '`' + strg + '`' + '\n'
        bot.send_message(message.chat.id, answer, parse_mode='Markdown')

    elif message.text == 'Ыч':
        show_menu()
        
    elif message.text == 'Скрыть':
        #close_menu()
        hide_menu()
        
    elif message.text == 'Закрыть':
        close_menu()

    elif message.text=='/zz': 
        markdown= '''**bold text**
            _italic text_
            [inline URL](http://www.example.com/)
            [inline mention of a user](tg://user?id=123456789)
            `inline fixed-width code`
            ```block_language
            pre-formatted fixed-width code block
            ```'''
        bot.send_message(message.chat.id, markdown, parse_mode='Markdown')
        
    else:
        bot.send_message(message.chat.id, "Шо?")
        

bot.polling( none_stop = True )
