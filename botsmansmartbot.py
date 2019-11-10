import pyowm
import telebot

owm = pyowm.OWM('55654dc1b5773bafd24ba70ab0b40ee4', language="ru")
bot = telebot.TeleBot("929266762:AAGMsHo5fflXm4YmCFJVdTWVNGcGtEYGgdM")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    command = message.text
    if "погода" in command:
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
        
    elif "прогноз погод" in command:
        fc = owm.three_hours_forecast('London,uk')
        f = fc.get_forecast()
        lst = f.get_weathers()
        
        answer = f
        
        for weather in f:
            answer += (weather.get_reference_time('iso'),weather.get_status()) + "/n"


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


