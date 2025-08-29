from src.data_loader import get_stock_data
from src.analysis import analyze_data
from src.model import train_model

if __name__ == "__main__":
    company_name = input("Enter company name or ticker: ")
    df, ticker = get_stock_data(company_name)  # ✅ expects 2 values

    if df is not None:
        df = analyze_data(df)
        train_model(df)
