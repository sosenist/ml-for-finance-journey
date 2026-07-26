daily_return = 0.025

if daily_return > 0:
    print("Gain today")
elif daily_return < 0:
    print("Loss today")
else:
    print("Flat day")


prices = [148.50, 150.25, 149.80, 152.10, 151.75]

for price in prices:
    print(f"Price: ${price:.2f}")

for i in range(5):
    print(f"Day {i}: price is {prices[i]}")

day = 0
while day < len(prices):
    print(f"While-loop day {day}: {prices[day]}")
    day += 1

for price in prices:
    if price > 151:
        print(f"Found a price above 151: {price} — stopping")
        break
    print(f"Checking price: {price}")

for price in prices:
    if price < 150:
        continue  # skip this one, go to next
    print(f"Price at or above 150: {price}")

volumes = [1200, 1500, 980, 2100, 1750]
for i in range(5):
    print(f"Day {i}: volume is {volumes[i]}")

day = 0
while day < len(volumes):
    print(f"While-loop day {day}: {volumes[day]}")
    day += 1

for volume in volumes:
    if volume > 2000:
        print(f"Found a volume above 2000: {volume} — stopping")
        break
    print(f"Checking volume: {volume}")

for volume in volumes:
    if volume < 1000:
        continue  # skip this one, go to next
    print(f"volume below 1000: {volume}")


# section 2


def simple_return(p0, p1):
    """Calculate the percentage return between two prices."""
    return (p1 - p0) / p0


result = simple_return(148.50, 150.25)
print(f"Return: {result:.4f}")
print(f"Return: {result * 100:.2f}%")


def returns_from_prices(prices):
    """Take a list of prices, return a list of daily returns."""
    daily_returns = []
    for i in range(1, len(prices)):
        r = simple_return(prices[i - 1], prices[i])
        daily_returns.append(r)
    return daily_returns


prices = [148.50, 150.25, 149.80, 152.10, 151.75]
rets = returns_from_prices(prices)
print(rets)


def classify_return(r):
    """Return 'gain', 'loss', or 'flat' based on a return value."""
    if r > 0:
        return "gain"
    elif r < 0:
        return "loss"
    else:
        return "flat"


for r in rets:
    print(f"{r*100:.2f}% -> {classify_return(r)}")


# TODO: loop through `prices` (not rets) using range(),
# and for each day print whether it's a "gain", "loss", or "flat"
# compared to the day before — i.e. combine what you built above
# Hint: you'll need simple_return() and classify_return() together, inside a loop


# exercise

prices = [144.50, 152.25, 142.80, 153.10, 151.75]

for i in range(1, len(prices)):
    r = simple_return(prices[i - 1], prices[i])
    label = classify_return(r)
    print(f"Day {i}: return = {r*100:.2f}% -> {label}")
