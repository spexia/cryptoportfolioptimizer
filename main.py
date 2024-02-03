from gethistoricaldata import get_historical_data,combine_stocks
import time,config
from pypfopt.expected_returns import mean_historical_return
from pypfopt.risk_models import CovarianceShrinkage

import PyPortfolioOpt


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


print(portfolio)

mu = mean_historical_return(portfolio)
S = CovarianceShrinkage(portfolio).ledoit_wolf()
