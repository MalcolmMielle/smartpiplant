'''
Documentation, License etc.

@package pythonplant
'''

#!/usr/bin/env python2
# -*- coding: utf-8-*-

from telegram import Updater
import logging
import serial
from pythonplant import *

# Enable logging
logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

logger = logging.getLogger(__name__)

plant1 = Plant()
plant2 = Plant()

ser = serial.Serial('/dev/ttyUSB0', 9600)
ser.timeout = None


list_chat = list()

def statusOfPlant(bot, update):
	#bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")
	#str = update.message.chat_id;
	#bot.sendMessage(chat_id=update.message.chat_id, text=str)
	bot.sendMessage(chat_id=update.message.chat_id, text="Plant 1 has that much water :")
	bot.sendMessage(chat_id=update.message.chat_id, text=plant1.water)
	bot.sendMessage(chat_id=update.message.chat_id, text="Plant 2 has that much water :")
	bot.sendMessage(chat_id=update.message.chat_id, text=plant2.water)
	
def register(bot, update):
	list_chat.append(update.message.chat_id);

def update(bot):
	print("update")
	updateValue(ser, plant1, plant2)
	if(plant1.is_thirsty() ):
		if(plant1.flag	 == True):
			plant1.flag = False
			for chat in list_chat:
				bot.sendMessage(chat_id=chat, text="Plant 1 need water :(")
	else:
		if(plant1.flag == False):
			plant1.flag = True
			for chat in list_chat:
				bot.sendMessage(chat_id=chat, text="Plant 1 is happy :D")
	if(plant2.is_thirsty() ):
		if(plant2.flag == True):
			plant2.flag = False
			for chat in list_chat:
				bot.sendMessage(chat_id=chat, text="Plant 2 need water :(")
	else:
		if(plant2.flag == False):
			plant2.flag = True
			for chat in list_chat:
				bot.sendMessage(chat_id=chat, text="Plant 2 is happy :D")


def main():	
	# Create the EventHandler and pass it your bot's token.
	updater = Updater("128116768:AAFsiMmSV7KjiN8xIidv7eX8TNgbnJ4zMLA")
	jobs = updater.job_queue
	jobs.put(update, 1, prevent_autostart=False)
	# Get the dispatcher to register handlers
	dp = updater.dispatcher

	dp.addTelegramCommandHandler('status',statusOfPlant)

	dp.addTelegramCommandHandler('register',register)

	# Start the Bot
	updater.start_polling()

	# Run the bot until the you presses Ctrl-C or the process receives SIGINT,
	# SIGTERM or SIGABRT. This should be used most of the time, since
	# start_polling() is non-blocking and will stop the bot gracefully.
	updater.idle()

if __name__ == '__main__':
	main()