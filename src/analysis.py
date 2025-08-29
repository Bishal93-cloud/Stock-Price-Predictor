import matplotlib.pyplot as plt

def analyze_data(df):
    print("\nFirst 5 rows:")
    print(df.head())

    # Feature engineering
    df["Daily Return"] = df["Close"].pct_change()
    df["SMA_20"] = df["Close"].rolling(window=20).mean()
    df["SMA_50"] = df["Close"].rolling(window=50).mean()

    # Plot Closing Price
    plt.figure(figsize=(10,6))
    plt.plot(df["Close"], label="Close Price")
    plt.title("Stock Closing Price")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()

    # Plot Moving Averages
    plt.figure(figsize=(12,6))
    plt.plot(df["Close"], label="Close Price")
    plt.plot(df["SMA_20"], label="SMA 20")
    plt.plot(df["SMA_50"], label="SMA 50")
    plt.title("Stock Price with Moving Averages")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()

    return df
