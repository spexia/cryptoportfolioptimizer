import csv,time,config,datetime
from binance.client import Client
import pandas as pd
from functools import reduce

client = Client(config.apiKey, config.secretKey)
start_time = config.start_time
end_time = config.end_time

def write(symbol, candlesticks):
    csvFileW = open(symbol + "_historical_data.csv", "w", newline="")
    klines_writer = csv.writer(csvFileW, delimiter=",")

    for candlestick in candlesticks:
        klines_writer.writerow(candlestick)

    csvFileW.close()

def get_historical_data(ticker):

    print("FETCHING DATA FOR: ", ticker)

    candlesticks = client.get_historical_klines(ticker, Client.KLINE_INTERVAL_1MINUTE, start_time, end_time)
    write(ticker, candlesticks)
    print("Data written for: ", ticker)

    csv_filename = f"{ticker}_historical_data.csv"
    attributes = ["timestamp", "open", "high", "low", "close", "volume", "1", "2", "3", "4", "5", "6"]
    df = pd.read_csv(csv_filename, names=attributes)

    converted_df = df[["timestamp","close"]]

    for timestamp in converted_df["timestamp"]:
        converted_df["timestamp"] = df["timestamp"].apply(lambda x: datetime.datetime.fromtimestamp(x/1000.0))
        
    converted_df.rename(columns = {'timestamp': 'date'},inplace = True)
    converted_df.rename(columns = {'close': f'{ticker}'},inplace = True)

    return converted_df

def combine_stocks(tickers):
    data_frames = []

    for i in tickers:
        print(i)
        data_frames.append(get_historical_data(i))

    df_merged = reduce(lambda left,right: pd.merge(left, right,on=['date'],how = 'outer'),data_frames)
    print(df_merged)

    return df_merged
