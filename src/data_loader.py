from yahooquery import search
import yfinance as yf
import os

# Ensure 'data' folder exists
if not os.path.exists("data"):
    os.makedirs("data")

def get_stock_data(company_name):
    results = search(company_name)
    quotes = results.get("quotes", [])

    if not quotes:
        print("❌ No matches found.")
        return None, None   # ✅ Always return 2 values

    # Show matches
    print("\n🔎 Matching Companies:")
    for i, q in enumerate(quotes, 1):
        print(f"{i}. {q['symbol']} → {q.get('shortname','No name')}")

    # User chooses
    try:
        choice = int(input("\nEnter the number of the company: ")) - 1
        if choice < 0 or choice >= len(quotes):
            print("❌ Invalid choice.")
            return None, None   # ✅ Always 2 values
    except ValueError:
        print("⚠️ Please enter a valid number.")
        return None, None

    ticker = quotes[choice]["symbol"]

    # Download historical data
    df = yf.Ticker(ticker).history(start="2015-01-01", auto_adjust=True)
    if df.empty:
        print("❌ No historical data found.")
        return None, None   # ✅ Always 2 values

    filename = f"data/{ticker}_data.csv"
    df.to_csv(filename)
    print(f"\n📈 Data for {ticker} downloaded successfully! Saved as {filename}")

    return df, ticker  # ✅ Correct: always 2 values
