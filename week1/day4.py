price = "130.22"

try:
    number = float(price)
    print(f"Converted: {number}")
except ValueError:
    print("That's not a valid number!")


def safe_divide(a, b):
    """Safely divide two numbers, handling division by zero."""
    try:
        return a / b
    except ZeroDivisionError:
        print("Can't divide by zero — returning None instead")
        return None


print(safe_divide(10, 2))
print(safe_divide(10, 0))

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Caught the error")
finally:
    print("This always runs, error or not")


with open("week1/sample_data.csv", "w") as f:
    f.write("date,price\n")
    f.write("2024-01-01,148.50\n")
    f.write("2024-01-02,150.25\n")
    f.write("2024-01-03,149.80\n")

with open("week1/sample_data.csv", "r") as f:
    for line in f:
        print(line.strip())


class Stock:
    def __init__(self, ticker, price, shares):
        self.ticker = ticker
        self.price = price
        self.shares = shares

    def value(self):
        return self.price * self.shares


apple = Stock("AAPL", 150.25, 10)
print(apple.ticker)
print(apple.value())

msft = Stock("MSFT", 310.50, 5)
print(msft.ticker, msft.value())
print(apple.ticker, apple.value())

nvda = Stock("NVDA", 280.50, 12)
print(nvda.ticker, nvda.value())
