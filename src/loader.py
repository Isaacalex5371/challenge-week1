import pandas as pd
import yfinance as yf
import os

class DataLoader:
    def __init__(self, data_path):
        self.data_path = data_path

    def load_news_data(self, filename):
        """Loads the financial news dataset."""
        file_path = os.path.join(self.data_path, filename)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        print(f"Loading news data from {file_path}...")
        df = pd.read_csv(file_path)
        
        # Convert date column to datetime
        if 'date' in df.columns:
            df['date'] = pd.to_datetime(df['date'], errors='coerce', utc=True)
            
        return df

    def load_stock_data(self, ticker, start_date="2020-01-01", end_date="2024-01-01"):
        """Downloads stock data from Yahoo Finance."""
        print(f"Downloading stock data for {ticker}...")
        stock_data = yf.download(ticker, start=start_date, end=end_date)
        
        # Handle MultiIndex columns if they exist (yfinance update)
        if isinstance(stock_data.columns, pd.MultiIndex):
            stock_data.columns = stock_data.columns.get_level_values(0)
            
        return stock_data