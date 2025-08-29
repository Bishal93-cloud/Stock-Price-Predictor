from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

def train_model(df):
    df = df.dropna()
    df["Target"] = df["Close"].shift(-1)
    df = df.dropna()

    features = ["Close", "SMA_20", "SMA_50", "Daily Return"]
    X = df[features].values
    y = df["Target"].values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    print(f"\n✅ Random Forest MSE: {mse:.2f}")

    # Plot
    plt.figure(figsize=(12,6))
    plt.plot(df.index[-len(y_test):], y_test, label="Actual Close")
    plt.plot(df.index[-len(y_test):], y_pred, label="Predicted Close")
    plt.title("Random Forest: Actual vs Predicted Closing Prices")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()
    pass