def simple_return(p0, p1):
    """Calculate the percentage return between two prices."""
    return (p1 - p0) / p0


def classify_return(r):
    """Return 'gain', 'loss', or 'flat' based on a return value."""
    if r > 0:
        return "gain"
    elif r < 0:
        return "loss"
    else:
        return "flat"


house_prices = [250000, 262000, 258000, 275000, 290000]

for year in range(1, len(house_prices)):
    last_year_price = house_prices[year - 1]
    this_year_price = house_prices[year]
    r = simple_return(last_year_price, this_year_price)
    label = classify_return(r)
    print(
        f"Year {year}: {last_year_price} -> {this_year_price}  |  return = {r*100:.2f}%  |  {label}")
