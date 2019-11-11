import pyowm
import telebot

owm = pyowm.OWM('55654dc1b5773bafd24ba70ab0b40ee4', language="ru")
bot = telebot.TeleBot("929266762:AAGMsHo5fflXm4YmCFJVdTWVNGcGtEYGgdM")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    command = message.text
    if "Погода" in command or "погода" in command:
        observation = owm.weather_at_place( 'Kyiv' )
        w=observation.get_weather()
        temp = w.get_temperature('celsius')["temp"]

        answer="В городе Киев сейчас "+w.get_detailed_status()+ "\n"
        answer+="Температура около "+ str(temp)+"\n\n"

        if temp < 10:
            answer += "Холодно шо писец, шубу одевай"
        elif temp < 20:
            answer += "Холодно, оденься"
        else:
            answer += "Нормас погода"

        bot.send_message(message.chat.id, answer)
        
    elif "Прогноз погод" in command or "прогноз погод" in command:
        fc = owm.three_hours_forecast( 'Kyiv' )
        f = fc.get_forecast()
        answer="/n"
        t1min=t2min=t3min=t4min=t5min=t6min=+100
        t1max=t2max=t3max=t4max=t5max=t6max=-100
        day1=day2=day3=day4=day5=day6=0
        mnt1=mnt2=mnt3=mnt41=mnt5=mnt6=0
        
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
 
            answer += (str(day1) + " , " + str(mnt1) + " : " + str(t1min) + " °C - " + str(t1max) + " °C;")
            answer += (str(day2) + " , " + str(mnt2) + " : " + str(t2min) + " °C - " + str(t2max) + " °C;")
            answer += (str(day3) + " , " + str(mnt3) + " : " + str(t3min) + " °C - " + str(t3max) + " °C;")
            answer += (str(day4) + " , " + str(mnt4) + " : " + str(t4min) + " °C - " + str(t4max) + " °C;")
            answer += (str(day5) + " , " + str(mnt5) + " : " + str(t5min) + " °C - " + str(t5max) + " °C;")
            answer += (str(day6) + " , " + str(mnt6) + " : " + str(t6min) + " °C - " + str(t6max) + " °C;")
        #answer = f

        bot.send_message(message.chat.id, answer)
        
        f2 = owm.daily_forecast( 'Kyiv' )
        lst = f2.get_forecast()
        answer = lst
        
        bot.send_message(message.chat.id, answer)
        
    elif message.text=='курс валют':
        bot.send_message(message.chat.id, 'А тебе то зачем? нищеброд))')

    else:
        bot.send_message(message.chat.id, message.text)

bot.polling( none_stop = True )

#owm=pyowm.OWM('55654dc1b5773bafd24ba70ab0b40ee4', language="ru")

#place = input("В каком городе?: ")

#observation = owm.weather_at_place(place)
#w=observation.get_weather()
#temp = w.get_temperature('celsius')["temp"]

#print(temp)
#print ("В городе " + place + " сейчас "+ w.get_detailed_status())
#print("Температура около "+ str(temp))


