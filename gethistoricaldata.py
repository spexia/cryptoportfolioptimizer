from gethistoricaldata import get_historical_data,combine_stocks
from opt import risk_return
from opt import gradient
from opt import scatter
import time,config
import pandas as pd
import matplotlib.pyplot as plt


print("==================================================")
print("==================================================")
print("Ｃｒｙｐｔｏ Ｐｏｒｔｆｏｌｉｏ Ｏｐｔｉｍｉｚｅｒ")
print("==================================================")
print("==================================================")

time.sleep(1)

symbollist = ['ETHUSDT','BTCUSDT','XRPUSDT','BCHUSDT','DOGEUSDT','SOLUSDT']

portfolio = combine_stocks(symbollist)
portfolio.to_csv("portfolio.csv", index=False)
portfolio = pd.read_csv("portfolio.csv")

results = pd.DataFrame(index=symbollist, columns=['X','Y'])

for symbol in symbollist:
    X, Y = risk_return(portfolio[symbol])
    results.loc[symbol] = [X,Y] 
    results.loc[symbol] = [X,Y] 

results['Color'] = results['Y'].apply(lambda val: gradient(val, results['Y'].min(), results['Y'].max()))

plt.figure(figsize=(10, 6))
for symbol, row in results.iterrows():
    scatter(row['X'], row['Y'], row['Color'], bar_scale=150, symbol = (f"INDEX:{symbol}"))

results['Weight'] = (results['Y'] / results['Y'].sum()) * 100


initial_investment = 100


print("Symbol\t\t\tWeight)")
print("----------------------------------------")
for symbol, row in results.iterrows():
    print(f"{(f'INDEX:{symbol}')}\t\t{row['Weight']:.4f}\t\t")


plt.xlabel("Risk (Standard Deviation)")
plt.ylabel("Return (Mean Daily Returns)")
plt.title("Modern Portfolio Theory")
plt.legend()
plt.show()
