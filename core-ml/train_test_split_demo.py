from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.linear_model import LinearRegression

size = np.array([650, 785, 1200, 1500, 1850, 2100, 2400]).reshape(-1, 1)
price = np.array([120, 145, 210, 260, 310, 350, 400])

model = LinearRegression()
model.fit(size, price)

# "Test" on the SAME data it just learned from
predictions = model.predict(size)
print("Actual: ", price)
print("Predicted:", predictions)


X_train, X_test, y_train, y_test = train_test_split(
    size, price, test_size=0.3, random_state=42
)

print("Train X:", X_train.ravel())
print("Test X:", X_test.ravel())


model = LinearRegression()
model.fit(X_train, y_train)   # only sees training data

test_predictions = model.predict(X_test)
print("Actual (test):   ", y_test)
print("Predicted (test):", test_predictions)
