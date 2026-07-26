tickers = ["AAPL", "MSFT", "GOOG", "AMZN", "TSLA"]

print(tickers[0])       # first item
print(tickers[-1])      # last item
print(tickers[1:3])     # slice: index 1 up to (not including) 3
print(tickers[:2])      # first two
print(tickers[2:])      # from index 2 to the end

tickers.append("NFLX")
print(tickers)

tickers.sort()
print(tickers)

tickers.remove("TSLA")
print(tickers)

print(len(tickers))


position = ("AAPL", 150.25, 10)
print(position)
print(position[0], position[1], position[2])

prices_by_ticker = {
    "AAPL": 150.25,
    "MSFT": 310.50,
    "GOOG": 2800.10,
    "AMZN": 3200.75,
    "TSLA": 245.30
}

print(prices_by_ticker["AAPL"])
print(prices_by_ticker.keys())
print(prices_by_ticker.values())

##
initial_value = 0
for value in prices_by_ticker.values():
    if value > initial_value:
        initial_value = value

print(f"highest value is", initial_value)

##
best_ticker = None
best_price = 0

for ticker, price in prices_by_ticker.items():
    if price > best_price:
        best_price = price
        best_ticker = ticker

print(f"Highest priced ticker is {best_ticker} at ${best_price}")


# sets
watchlist = {"AAPL", "MSFT", "GOOG"}
portfolio = {"MSFT", "TSLA", "AMZN"}

print("AAPL" in watchlist)      # membership check
print("TSLA" in watchlist)

print(watchlist & portfolio)    # intersection: in both
print(watchlist | portfolio)    # union: in either
print(watchlist - portfolio)    # difference: in watchlist but not portfolio

##

squares = []
for x in range(5):
    squares.append(x ** 2)
print(squares)

# The comprehension way — same result, one line:
squares_v2 = [x ** 2 for x in range(5)]
print(squares_v2)


# Loop version
doubled = []
for x in [1, 2, 3, 4]:
    doubled.append(x * 2)
print(doubled)   # [2, 4, 6, 8]

# Comprehension version — exact same thing
doubled_v2 = [x * 2 for x in [1, 2, 3, 4]]
print(doubled_v2)   # [2, 4, 6, 8]

prices = [148.50, 150.25, 149.80, 152.10, 151.75]

rounded = [round(x) for x in prices]
print(rounded)


prices = [148.50, 150.25, 149.80, 152.10, 151.75]

# Only keep prices above 150
high_prices = [p for p in prices if p > 150]
print(high_prices)

low_prices = [p for p in prices if p < 150]
print(low_prices)

low_prices = []
for price in prices:
    if price < 150:
        low_prices.append(price)
print(low_prices)


# Double only the prices that are above 150
result = [price * 2 for price in prices if price > 150]
print(result)


prices_by_ticker = {
    "AAPL": 150.25,
    "MSFT": 310.50,
    "GOOG": 2800.10,
    "AMZN": 3200.75,
    "TSLA": 245.30
}

# Regular loop version first
rounded_dict = {}
for ticker, price in prices_by_ticker.items():
    rounded_dict[ticker] = round(price)
print(rounded_dict)

# Comprehension version — same result
rounded_dict_v2 = {ticker: round(price)
                   for ticker, price in prices_by_ticker.items()}
print(rounded_dict_v2)


raw = "AAPL:150.2,MSFT:310.5,GOOG:2800.1"

parts = raw.split(",")
print(parts)

for part in parts:
    ticker, price = part.split(":")
    print(f"Ticker: {ticker}, Price: {price}")


# TODO: parse `raw` into a dictionary like {"AAPL": 150.2, "MSFT": 310.5, "GOOG": 2800.1}
# Hints:
# - start with an empty dict: parsed = {}
# - split raw by "," first, then each part by ":"
# - convert the price string to a float before storing it
# - store it with parsed[ticker] = price

parsed = {}

parts = raw.split(",")
print(parts)

parts = raw.split(":")
print(parts)

parsed = dict(item.split(":") for item in raw.split(","))

for key, value in parsed.items():
    parsed[key] = float(value)
