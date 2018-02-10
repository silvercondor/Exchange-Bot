import requests, json
from bs4 import BeautifulSoup

# Function to process CMC's api to retrieve the name of coin based on symbol provided
def updateDB(database):

	# Might want to include error handling just in case
	print("Updating database...")
	page = requests.get("https://api.coinmarketcap.com/v1/ticker/?limit=0")
	response = json.loads(page.text)

	# Convert list of dict into dict of dict
	for i in response:
		database[i.get('symbol')] = i
	print("Update complete!")

# Function to check if coin exists in coin_to_exchanges dictionary
def checkCoin(coin, coin_to_exchanges):
	if(coin in coin_to_exchanges):
		print(coin + " found!")
		return True
	print(coin + " not found!")
	return False

# Function to get html source code for coin
def getSource(coin):
	print("In getSource function")
	url = 'https://coinmarketcap.com/currencies/' + coin + '/'
	page = requests.get(url)
	if(page.status_code == 404):
		print("Source code not found")
		return False
	else:
		print("Source code found!")
		return BeautifulSoup(page.content, 'html.parser')

# Function to add coin to existing list
def updateCoin(coin, coin_to_exchanges):
	print("In updateCoin function")
	# Get source code
	soup = getSource(coin)

	# Process source code to get unique list of exchanges for coin
	if(soup != False):
		body = list(soup.find('table', id='markets-table').children)[3]
		i = 1
		rows = list(body.children)

		# Using sets instead of 
		exchanges = set()
		while(i < len(rows)):
			exchange = (list(rows[i])[3]).get_text()
			exchanges.add(exchange)
			i = i + 2
		coin_to_exchanges[coin] = exchanges
		print(coin + " updated!")
	else:
		print("Error retrieving Source Code")


# Function to get list of exchanges for the given coin
def getExchange(coin, coin_to_exchanges):
	# If coin_to_exchanges doesn't contain coin, add it in. 
	if(not checkCoin(coin,coin_to_exchanges)):
		print("Processing exchange data for " + coin)
		updateCoin(coin, coin_to_exchanges)
		try:
			return coin_to_exchanges[coin]
		except Exception as e:
			print(e)
			return False
	else:
		return coin_to_exchanges[coin]
		
# Function to update an existing list of exchanges for the given coin
# This function doesn't have a handler yet.
def updateExchange(coin, coin_to_exchanges):
	if(not checkCoin(coin, coin_to_exchanges)):
		print("Updating exchange data for " + coin)
		updateCoin(coin, coin_to_exchanges)


	
