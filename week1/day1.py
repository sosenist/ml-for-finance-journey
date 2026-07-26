# Variables and types
price = 150.25
shares = 10
ticker = "AAPL"
is_profitable = True

print(f"You own {shares} shares of {ticker} at ${price} each")
print(f"Total position value: ${price * shares}")
print(type(price), type(shares), type(ticker), type(is_profitable))


price_input = input("Enter a stock price: ")
shares_input = input("Enter number of shares: ")

price = float(price_input)
shares = int(shares_input)

total_value = price * shares
print(f"Total position value: ${total_value:.2f}")

celsius = 22
fahrenheit = celsius * 9/5 + 32
print(f"{celsius}°C is {fahrenheit}°F")

price_yesterday = 148.50
price_today = 150.25

daily_return = (price_today - price_yesterday) / price_yesterday
print(f"Daily return: {daily_return:.4f}")
print(f"Daily return: {daily_return * 100:.2f}%")

messy = 0.1 + 0.2
print(messy)          # try guessing before running this
print(f"{messy:.2f}")
