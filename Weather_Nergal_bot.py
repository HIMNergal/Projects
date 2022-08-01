from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
import telebot

owm = OWM('bdac83794cc92b2fa064732adfb99a4d')

bot = telebot.TeleBot("5276418433: AAERykbiX8Rux4acSITzcRYbB6NT_HV4f3U", parse_mode=None)

@bot.message_handler(content_types=['text'])
def send_welcome(message):

    observation = mgr.weather_at_place (message.text )
    w = observation.weather
    temp = w.temperature('celsius') ["temp"]
    answer = "В городе " + message.text + " сейчас " + w.detailed_status() + "\n"
    answer += "Температура сейчас в районе " + str(temp) + "\n\n"

    if temp < 10:
	    answer += "Сейчас довольно холодно, одевайтесь теплее!"
    elif temp > 20:
	    answer += "На улице тепло, прекрасная погода для прогулки!"
    else:
	    answer += "На улице прохладно, не забудьте шапку!"

