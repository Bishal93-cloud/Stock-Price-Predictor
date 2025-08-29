# 📈 Stock Price Predictor & Analyzer

This Python project fetches historical stock data, performs basic analysis with feature engineering, visualizes the data, and provides a framework for training a prediction model.

## Features ✨

* **Dynamic Ticker Search**: Enter a company name (e.g., "Apple" or "Reliance") and the script finds matching stock tickers for you to choose from.
* **Data Downloader**: Fetches historical stock data from Yahoo Finance and saves it as a CSV file.
* **Data Analysis**: Calculates daily returns and simple moving averages (SMA).
* **Visualization**: Plots the stock's closing price and its moving averages using Matplotlib.

## Project Structure 📂

The project is organized into a `src` (source) directory to keep the code clean and modular.

```
Stock Price Predictor/
├── data/               # Downloaded stock CSV files will be saved here
├── src/
│   ├── __init__.py
│   ├── data_loader.py  # Handles fetching and loading data
│   ├── analysis.py     # Performs and visualizes data analysis
│   ├── model.py        # Contains the machine learning model
│   └── main.py         # The main script to run the application
└── requirements.txt    # Lists all the project dependencies
```

## How to Use 🚀

1.  **Clone the Repository**
    ```bash
    git clone [your-github-repo-link]
    cd Stock-Price-Predictor
    ```

2.  **Install Dependencies**
    Make sure you have Python installed. Then, run the following command in your terminal to install the necessary libraries:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Application**
    Execute the main script from the project's root directory:
    ```bash
    python src/main.py
    ```
    The script will then prompt you to enter a company name. Based on your choice, it will download the data and display the analysis plots.

## A Quick Note on Your `model.py`

I noticed the code for `model.py` was the same as `analysis.py`. To make your project run, here is a simple placeholder for your `model.py` file. You can replace this later with your actual machine learning model (like an LSTM or Linear Regression).

```python
# src/model.py

def train_model(df):
    """
    A placeholder function for training a stock prediction model.
    """
    print("\n[INFO] Model training step...")
    
    if 'Close' in df.columns:
        print("Data received. Ready to train a model on the 'Close' price.")
        # --- Your machine learning code will go here ---
        print("[SUCCESS] Model training placeholder complete.")
    else:
        print("[ERROR] DataFrame does not contain 'Close' column.")

```