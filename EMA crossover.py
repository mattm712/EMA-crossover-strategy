#import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import datetime
import yfinance as yf
import matplotlib.pyplot as plt


#define time period
START = datetime.datetime(2000, 1, 1)
END = datetime.datetime(2025, 1, 1)
YEARS = (END - START).days / 365.25


#import data and remove unused columns
symbol = "SMH"
price = yf.download(symbol, start=START, end=END, auto_adjust=True)
price = price.drop(['High', 'Low','Volume'], axis=1)
print(price.head())
print(price.tail())


#define MA variables
FAST_MA = 50
SLOW_MA = 200
STARTING_BALANCE = 10000


#calculate daily returns and add to matrix
price['Return'] = price.Close / price.Close.shift(1)
price['Bench_Bal'] = STARTING_BALANCE * price.Return.cumprod()
print(price.head())
print(price.tail())


#calculate drawdown (MDD)
price['Bench_Peak'] = price.Bench_Bal.cummax()
price['Bench_DD'] = price.Bench_Bal - price.Bench_Peak
bench_dd = round(((price.Bench_DD / price.Bench_Peak).min()) * 100,2)
print(price.head())
print(price.tail())
print(bench_dd)


#calculate moving averages
price['Fast_EMA'] = price['Close'].ewm(span=FAST_MA, adjust=False).mean()
price['Slow_EMA'] = price['Close'].ewm(span=SLOW_MA, adjust=False).mean()
price.dropna(inplace=True)
print(price.head())
print(price.tail())


#draw graph of moving averages
plt.figure(figsize=(14,6))
plt.plot(price.Close)
plt.plot(price.Fast_EMA, color ="red")
plt.plot(price.Slow_EMA, color ="blue")
plt.show()


#define entries
price['Long'] = price.Fast_EMA > price.Slow_EMA
print(price.head())


#calculate system balance
price['Sys_Ret'] = np.where(price.Long.shift(1) == True, price.Return,1)
price['Sys_Bal'] = STARTING_BALANCE * price.Sys_Ret.cumprod()
print(price.tail())

#calculate drawdown
price['Sys_Peak'] = price.Sys_Bal.cummax()
price['Sys_DD'] = price.Sys_Bal - price.Sys_Peak
sys_dd = round((((price.Sys_DD / price.Sys_Peak).min()) * 100), 2)
print(sys_dd)


#calculate metrics
bench_return = round(((price.Bench_Bal.iloc[-1]/price.Bench_Bal.iloc[1]) - 1) * 100, 2)
bench_cagr = round(((((price.Bench_Bal.iloc[-1]/price.Bench_Bal.iloc[1])**(1/YEARS))-1)*100), 2)
sys_return = round(((price.Sys_Bal.iloc[-1]/price.Sys_Bal.iloc[0]) - 1) * 100, 2)
sys_cagr = round((((price.Sys_Bal.iloc[-1]/price.Sys_Bal.iloc[0])**(1/YEARS)-1)*100), 2)
sys_tim = round((price.Long.sum() / price.shape[0]) * 100, 2)

print(f'Benchmark Total return: {bench_return}%')
print(f'Benchmark CAGR: {bench_cagr}')
print(f'Benchmark DD: {bench_dd}%')
print('')
print(f'System Total return: {sys_return}%')
print(f'System CAGR: {sys_cagr}')
print(f'System DD: {sys_dd}%')
print(f'System Time in the Market: {sys_tim}%')
