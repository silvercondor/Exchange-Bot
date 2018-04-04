# Exchange-Bot
### Exchange Bot for cryptocurrencies

Library: [Python-Telegram-Bot](https://github.com/python-telegram-bot/python-telegram-bot)

Goal: To determine which exchange you can buy a coin from.

#### Instructions:

1. Create a file called token.txt with the Bot Api.
2. Replace the location in line 15 with the location of your token.txt file.
3. Run Python3 ExchangeBot.py (Make sure you have Requests and BeautifulSoup installed)
4. Once the program is running, run the updateDB command which will update the internal database (dictionary) using CoinMarketCap's API. The DB will consist of coin name, ticker pairs. 
5. To determine the exchange, run the command exchange followed by a ticker. 

#### Notes:
- When the exchange command is run for a coin for the first time, the code will scrape off CoinMarketCap via BeautifulSoup and Requests. This means 2 things:
  1. If CMC's website structure changes, the code will break.
  2. If the list of exchanges is updated, the cached results will need to be updated.
- To update the cached results, run the updateExchange command.

#### Issues to be fixed
- [X] Determine how to handle coins with the same ticker, try KNC.

#### Upcoming Features
- [ ] Add description to my commands when typing /command in Telegram
- [X] Sorting exchanges by volume and what the trade volume is for that exchange
- [ ] Determining the difference between the coins listed on 2 exchanges

#### Additional Functionality 
- [ ] Accumulation Tracker (Progress halted indefinitely for now)
