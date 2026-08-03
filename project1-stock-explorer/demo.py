import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

tickers = ["AAPL", "MSFT", "GOOG", "AMZN"]

# 1. Download data for each ticker, store in a dictionary
data_dict = {}
for ticker in tickers:
    df = yf.download(ticker, start='2026-01-01',
                     end='2026-07-01', progress=False)
    data_dict[ticker] = df

print(data_dict)
