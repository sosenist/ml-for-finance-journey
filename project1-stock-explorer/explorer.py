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

# 2. Compute daily returns and rolling volatility for each ticker
returns_dict = {}
volatility_dict = {}

for ticker, df in data_dict.items():
    if not df.empty:
        # force plain Series, avoids nested-column issue
        close_prices = df['Close'].squeeze()
        daily_return = close_prices.pct_change()

        returns_dict[ticker] = daily_return
        volatility_dict[ticker] = daily_return.rolling(20).std()

        print(f"--- Last 5 daily returns for {ticker} ---")
        print(daily_return.tail())
        print(f"--- Last 5 rolling volatility values for {ticker} ---")
        print(volatility_dict[ticker].tail())

# 3. Build a summary table comparing mean return and volatility across tickers
summary = {}
for ticker, df in data_dict.items():
    if not df.empty:
        close_prices = df['Close'].squeeze()
        daily_return = close_prices.pct_change()
        summary[ticker] = {
            "mean_return": daily_return.mean(),
            "volatility": daily_return.std()
        }

summary_df = pd.DataFrame(summary).T
print("\n--- Summary: mean return & volatility across tickers ---")
print(summary_df)

# 4. Plot normalized prices so all tickers are comparable despite different price scales
plt.figure(figsize=(10, 6))

for ticker, df in data_dict.items():
    if not df.empty:
        close_prices = df['Close'].squeeze()
        normalized = close_prices / close_prices.iloc[0] * 100
        plt.plot(df.index, normalized, label=ticker)

plt.title("Normalized Price Comparison (Start = 100)")
plt.xlabel("Date")
plt.ylabel("Normalized Price")
plt.legend()
plt.savefig("project1-stock-explorer/charts/price_comparison.png")
plt.show()
