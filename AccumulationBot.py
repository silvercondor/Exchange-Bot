# Import libraries
import requests
import json

# Retrieve token from external file
f = open('/Users/simon/Documents/Github/Python/Accumulation Tracker/token.txt', 'r')
tokenId = f.readline()

# Retrieveing the api
page = requests.get("https://api.coinmarketcap.com/v1/ticker/?limit=10")

# Parsing API into a list of dict.
response = json.loads(page.text)

# Converting the list of dict into a dict of values