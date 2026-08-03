# 1. Imports + data
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

size = np.array([650, 785, 1200, 1500, 1850, 2100, 2400])
price = np.array([120, 145, 210, 260, 310, 350, 400])

print(size)
print(price)

# 2. Scatter plot (Step 1)
plt.scatter(size, price)
plt.xlabel("Size (sq ft)")
plt.ylabel("Price ($1000s)")
plt.title("House Size vs Price")
plt.show()

# 3. Manual fit with polyfit (Step 2) — defines new_size and predicted_price
slope, intercept = np.polyfit(size, price, 1)
print(f"slope: {slope:.4f}, intercept: {intercept:.4f}")

new_size = 1700
predicted_price = slope * new_size + intercept
print(f"Predicted price for {new_size} sq ft: ${predicted_price:.1f}k")

# 4. Visualize the fitted line (Step 3) — this is what's currently erroring
plt.scatter(size, price, label="Actual data")
plt.plot(size, slope * size + intercept, color="red", label="Fitted line")
plt.scatter([new_size], [predicted_price],
            color="green", s=100, label="Prediction")
plt.xlabel("Size (sq ft)")
plt.ylabel("Price ($1000s)")
plt.legend()
plt.show()

# 5. scikit-learn version (Step 4)

X = size.reshape(-1, 1)
y = price

model = LinearRegression()
model.fit(X, y)

print(f"slope (coefficient): {model.coef_[0]:.4f}")
print(f"intercept: {model.intercept_:.4f}")

new_size_array = np.array([[1700]])
prediction = model.predict(new_size_array)
print(f"Predicted price: ${prediction[0]:.1f}k")
