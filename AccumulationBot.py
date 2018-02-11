# Import libraries
import telegram
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import functions
from random import randint

# if __name__ == "__main__":
# 	main()

# # Main code
# def main():

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

# Command to update database
def updateDB(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text='Updating database...')
	functions.updateDB(database)
	bot.send_message(chat_id=update.message.chat_id, text='Update complete!')
updateDB_handler = CommandHandler('updateDB', updateDB)
dispatcher.add_handler(updateDB_handler)


# Command to find all exchanges that trades this coin
def exchange(bot, update, args):
	print()
	if(len(args) != 1):
		bot.send_message(chat_id=update.message.chat_id, text='Too few / many arguments! Please enter only 1 ticker.', reply_to_message_id=update.message.message_id)
	else:
		# Getting the id equivalent (full name delimited with '-') of the target coin
		coin = args[0].upper()
		if(coin in database):
			id = database[coin].get('id')
			exchanges = functions.getExchange(id, coin_to_exchanges)
			if(exchanges):
				print("Printing exchanges...")

				# list_of_exchanges is a list of concatenated exchanges into strings with a maximum length of 4096 characters, see comments in the concatExchange Function as to why this isn't necessary for now.
				# list_of_exchanges = []
				
				list_of_exchanges = functions.concatExchanges(exchanges)
				bot.send_message(chat_id=update.message.chat_id, text=list_of_exchanges, reply_to_message_id=update.message.message_id)
				#for i in list_of_exchanges:
					#bot.send_message(chat_id=update.message.chat_id, text=i, reply_to_message_id=update.message.message_id)
		else:
			print(args[0] + " not found!")
			bot.send_message(chat_id=update.message.chat_id, text=args[0] + " cannot be found in DB, please run the updateDB command or check that you've entered a valid ticker.", reply_to_message_id=update.message.message_id)

exchange_handler = CommandHandler('exchange', exchange, pass_args=True)
dispatcher.add_handler(exchange_handler)

# Command to update list of exchanges that trades this coin
def updateExchange(bot, update, args):
	print()
	if(len(args) != 1):
		bot.send_message(chat_id=update.message.chat_id, text='Too few / many arguments! Please enter only 1 ticker.', reply_to_message_id=update.message.message_id)
	else:
		# Getting the id equivalent (full name delimited with '-') of the target coin
		coin = args[0].upper()
		if(coin in database):
			id = database[coin].get('id')
			functions.updateExchange(id, coin_to_exchanges)
			bot.send_message(chat_id=update.message.chat_id, text="Exchanges for " + args[0] + " is updated!", reply_to_message_id=update.message.message_id)
		else:
			print(args[0] + " not found!")
			bot.send_message(chat_id=update.message.chat_id, text=args[0] + " cannot be found in DB, please run the updateDB command or check that you've entered a valid ticker.", reply_to_message_id=update.message.message_id)

updateExchange_handler = CommandHandler('updateExchange', updateExchange, pass_args=True)
dispatcher.add_handler(updateExchange_handler)


# Command to handle unregistered commands
def unknown(bot, update):
	replies = ["Stop trolling my bot Brian!", "Invalid command...", "Please try again later even though it'll probably still not work lol.", "404 Error: Command not found!"]
	bot.send_message(chat_id=update.message.chat_id, text=replies[randint(0,3)], reply_to_message_id=update.message.message_id)

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)



# Start the bot
print('starting bot!')
updater.start_polling(clean=True)


# Additional Features

# Move functions to function.py, leave the messagehandler and add handler in this file under a main function
# Add description to commands
# Send hyperlink instead of just name, use name as text in a href
# Add volume
## 2 coins w/ same ticker fail, see knc

# and the actual acccumulation part lol