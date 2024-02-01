from binance import Client
import config
import csv

client = Client(config.apiKey, config.secretKey)
symbolList = input("Please enter a symbol : (BTCUSDT)")
