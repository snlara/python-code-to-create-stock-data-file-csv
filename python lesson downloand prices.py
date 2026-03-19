import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# 1. Define the ticker and the timeframe
ticker_symbol = "SPY"
end_date = datetime.now().strftime('%Y-%m-%d')
start_date = (datetime.now() - timedelta(days=20*365)).strftime('%Y-%m-%d')

# 2. Pull the data
print(f"Fetching data for {ticker_symbol}...")
spy_data = yf.download(ticker_symbol, start=start_date, end=end_date)

# 3. Save to CSV
file_name = "SPY_20y_data.csv"
spy_data.to_csv(file_name)

print(f"Success! Data saved to {file_name}")
print(spy_data.head()) # Preview the first 5 rows