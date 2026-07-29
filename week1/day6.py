import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd

data = {
    "ticker": ["AAPL", "MSFT", "GOOG", "AMZN"],
    "price": [150.25, 310.50, 2800.10, 3200.75],
    "shares": [10, 5, 2, 3]
}

df = pd.DataFrame(data)

print(df["price"])           # one column, as a "Series"
print(df[["ticker", "price"]])  # multiple columns, as a DataFrame

print(df.loc[0])             # first row, by label/index
print(df.iloc[0])            # first row, by position
print(df.iloc[1:3])          # rows 1 and 2 (position-based slicing)


df["position_value"] = df["price"] * df["shares"]
print(df)


###


data = yf.download("AAPL", period="6mo")
print(data.head())
print(data.shape)


data["daily_return"] = data["Close"].pct_change()
print(data[["Close", "daily_return"]].head(10))

print(f"Mean daily return: {data['daily_return'].mean():.4%}")
print(f"Daily volatility (std): {data['daily_return'].std():.4%}")
print(f"Best day: {data['daily_return'].max():.4%}")
print(f"Worst day: {data['daily_return'].min():.4%}")


ticker = "AAPL"
data = yf.download(ticker, period="6mo")
data["daily_return"] = data["Close"].pct_change()

print(f"--- {ticker} summary (6 months) ---")
print(f"Mean daily return: {data['daily_return'].mean():.4%}")
print(f"Daily volatility: {data['daily_return'].std():.4%}")
print(f"Best day: {data['daily_return'].max():.4%}")
print(f"Worst day: {data['daily_return'].min():.4%}")

plt.figure(figsize=(10, 5))
plt.plot(data.index, data["Close"])
plt.title(f"{ticker} Closing Price — Last 6 Months")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.savefig("week1/aapl_price_chart.png")
plt.show()
