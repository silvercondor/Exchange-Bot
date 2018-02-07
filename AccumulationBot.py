# Import libraries
import requests
from bs4 import BeautifulSoup
import telegram
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Initiate logging module
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

# Retrieve token from external file
f = open('/Users/simon/Documents/Github/Accumulation Tracker/token.txt', 'r')
tokenId = f.readline()

# Create bot object and its corresponding updater and dispatcher
bot = telegram.Bot(token=tokenId)
updater = Updater(token=tokenId)
dispatcher = updater.dispatcher 

# Function to get html source code
def getSource(coin):
	url = 'https://coinmarketcap.com/currencies/' + coin + '/'
	page = requests.get(url)
	if(page.status_code == 404):
		return False
	else:
		return BeautifulSoup(page.content, 'html.parser')
	
# Function to get list of exchanges 
def getExchange(coin):
	soup = getSource(coin)
	if(soup != False):
		body = list(soup.find('table', id='markets-table').children)[3]
		i = 1
		rows = list(body.children)
		while(i < len(rows)):
			
			exchange = (list(rows[i])[3]).get_text()
			print(str(i) + " " + exchange)
			i = i + 2

		
		#print(list(list(test.children)[3].children)[0].get_text())
	else:
		#instead of printing error, i should just initialize body to sth
		print("error")

	
	
	#i = 1;
	#while(i < len(list(body.children))):
	# https://stackoverflow.com/questions/3817529/syntax-for-creating-a-dictionary-into-another-dictionary-in-python

getExchange('Cindicator')

# function to remove duplicates
# https://stackoverflow.com/questions/7961363/removing-duplicates-in-lists

# id="markets-table" class="table no-border table-condensed dataTable no-footer"

# # Creating an exchange command to find all exchanges that trades this coin
# def exchange(bot, update, args):
# 	listOfExchanges = ....
# 	bot.send_message(chat_id=update.message.chat_id, text=text_caps)

# exchange_handler = CommandHandler('exchange', exchange, pass_args=True)
# dispatcher.add_handler(exchange_handler)




########## future features ############
# Every X mins update dict (use ticker instead of full name) 
# store somewhere if coin found b4, no need to repeat query unless each coin has a flag to determine when it should rerun query.