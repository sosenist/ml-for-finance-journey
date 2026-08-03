from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import yfinance as yf
import numpy as np

data = yf.download("AAPL", period="1y")
data["daily_return"] = data["Close"].squeeze().pct_change()
data = data.dropna()

print(data.shape)
print(data.index[0], "to", data.index[-1])

# Target: was tomorrow a gain (1) or not (0)?
data["target"] = (data["daily_return"].shift(-1) > 0).astype(int)

# Feature: today's return, used to predict tomorrow's direction
data["feature_lag1"] = data["daily_return"]
data = data.dropna()

print(data[["daily_return", "feature_lag1", "target"]].tail())


# double brackets -> DataFrame, which is what sklearn wants for X
X = data[["feature_lag1"]]
y = data["target"]            # single bracket -> Series, which is fine for y

print(X.shape, y.shape)


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=45
)

model = LogisticRegression()
model.fit(X_train, y_train)
print(f"Accuracy (random split): {model.score(X_test, y_test):.2%}")

X_train2, X_test2, y_train2, y_test2 = train_test_split(
    X, y, test_size=0.3, shuffle=False
)

model2 = LogisticRegression()
model2.fit(X_train2, y_train2)
print(f"Accuracy (time-based split): {model2.score(X_test2, y_test2):.2%}")

print(X_train2.index[-1])
