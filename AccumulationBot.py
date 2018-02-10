# Import libraries
import telegram
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import functions

# Initiate logging module
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

# Retrieve token from external file
f = open('/Users/simon/Documents/Github/Accumulation Tracker/token.txt', 'r')
tokenId = f.readline()

# Create bot object and its corresponding updater and dispatcher
bot = telegram.Bot(token=tokenId)
updater = Updater(token=tokenId)
dispatcher = updater.dispatcher 

# Initializing a dictionary of coin exchanges pairs
coin_to_exchanges = dict()

# Initialize a dict of dictionaries for database
database = dict()

# Function to update database
def updateDB(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text='Updating database...')
	functions.updateDB(database)
	bot.send_message(chat_id=update.message.chat_id, text='Update complete!')
updateDB_handler = CommandHandler('updateDB', updateDB)
dispatcher.add_handler(updateDB_handler)


# Creating an exchange command to find all exchanges that trades this coin
def exchange(bot, update, args):
	# To do: count length of message, instead of sending multiple messages just combine all in 1. 

	print()

	if(len(args) != 1):
		bot.send_message(chat_id=update.message.chat_id, text='Too few / many arguments! Please enter only 1 ticker.')
	else:
		# Getting the id equivalent (full name delimited with '-') of the target coin
		coin = args[0].upper()
		if(coin in database):
			id = database[coin].get('id')
			exchanges = functions.getExchange(id, coin_to_exchanges)
			if(exchanges):
				print("Printing exchanges...")
				for i in exchanges:

					############################## I think it's timing out cause i'm sending too many messages to the server
					bot.send_message(chat_id=update.message.chat_id, text=i)
		else:
			print(args[0] + " not found!")
			bot.send_message(chat_id=update.message.chat_id, text=args[0] + " cannot be found in DB, please run the updateDB command or check that you've entered a valid ticker.")

exchange_handler = CommandHandler('exchange', exchange, pass_args=True)
dispatcher.add_handler(exchange_handler)

# Start the bot
print('starting bot!')
updater.start_polling(clean=True)