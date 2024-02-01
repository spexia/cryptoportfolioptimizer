import csv
from binance.client import Client
import time
import config

client = Client(config.apiKey, config.secretKey)

def write(symbol, candlesticks):
    csvFileW = open(symbol + "_historical_data.csv", "w", newline="")
    klines_writer = csv.writer(csvFileW, delimiter=",")

    for candlestick in candlesticks:
        klines_writer.writerow(candlestick)

    csvFileW.close()

def get_historical_data():
    symbols = input("Please enter symbols (BTC,ETH): ").split(' ')
    startdate = input("Please enter start date (November 3, 2023): ")
    enddate = input("Please enter end date (November 5, 2023): ")
    candletime = input("Please enter time interval (1): ")

    time.sleep(2)

    print(f"Selected symbols are: {symbols}\nstartdate: {startdate}, enddate: {enddate}\ntime interval: {candletime} MINUTE")

    time.sleep(1)
    
    for symbol in symbols:
        print("FETCHING DATA FOR: ", symbol)
        symbol_with_usdt = symbol + "USDT"

        kline_interval = getattr(Client, f"KLINE_INTERVAL_{candletime}MINUTE")

        candlesticks = client.get_historical_klines(symbol_with_usdt, kline_interval, startdate, enddate)
        write(symbol, candlesticks)
        print("Data written for: ", symbol)
