# EMA Crossover Trading Strategy Backtest

This repository contains a Python script to backtest a simple **Exponential Moving Average (EMA) Crossover Trading Strategy** on stock or index data downloaded via Yahoo Finance.

---

## Overview

The strategy uses two EMAs of the closing price:

- **Fast EMA** (shorter period, e.g. 9, 50 days)
- **Slow EMA** (longer period, e.g. 21, 200 days)

### Trading Rule:
- Go **Long** (buy) when the Fast EMA crosses above the Slow EMA.
- Exit the position (go to cash) when the Fast EMA crosses below the Slow EMA.

The script compares this strategy against a buy-and-hold benchmark and calculates key performance metrics such as total return, CAGR, maximum drawdown, and time spent in the market.

---

## Features

- Download historical price data from Yahoo Finance using `yfinance`
- Calculate Fast and Slow EMAs
- Generate entry signals based on EMA crossovers
- Compute system returns and balance
- Calculate maximum drawdown for both system and benchmark
- Output performance metrics:
  - Total return (%)
  - CAGR (%)
  - Maximum Drawdown (%)
  - Time in the market (%)
- Visualize closing prices with EMA overlays

# Modify these parameters in the script:

```python
symbol = "SMH"                 # Ticker symbol, e.g., 'SPY', 'TSLA', 'AAPL'
FAST_MA = 50                  # Fast EMA period
SLOW_MA = 200                 # Slow EMA period
STARTING_BALANCE = 10000      # Initial capital for backtest
START = datetime.datetime(2000, 1, 1)  # Backtest start date
END = datetime.datetime(2025, 1, 1)    # Backtest end date
```
## Results

This EMA crossover strategy, applied to the SMH ETF with a 50-day fast EMA and a 200-day slow EMA, has demonstrated strong performance over the backtested period (2000–2025). Compared to a simple buy-and-hold benchmark, the strategy delivered:

- A **higher total return (1051.94%)** and **improved CAGR (10.27%)**, outperforming the benchmark's 491.14% total return and 7.37% CAGR.
- A **significantly lower maximum drawdown (-33.62%)**, reducing downside risk relative to the benchmark’s drawdown of -85.92%.
- A **time in the market of approximately 63%**, indicating the strategy avoided major market downturns by stepping out during bearish trends.

These results suggest that the 50/200 EMA crossover can be an effective trend-following strategy for managing risk and enhancing returns in the semiconductor sector.

