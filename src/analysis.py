import pandas as pd
import numpy as np

class NewsAnalyzer:
    def __init__(self, df):
        self.df = df

    def get_headline_stats(self):
        """Returns basic statistics about headline lengths."""
        self.df['headline_len'] = self.df['headline'].astype(str).apply(len)
        return self.df['headline_len'].describe()

    def get_top_publishers(self, n=10):
        """Returns the top N publishers."""
        return self.df['publisher'].value_counts().head(n)

    def get_daily_publication_counts(self):
        """Returns the count of articles per day."""
        return self.df.set_index('date').resample('D').size()

class StockAnalyzer:
    def __init__(self, stock_df):
        self.stock_df = stock_df

    def add_moving_average(self, window=20):
        """Adds Simple Moving Average (SMA)."""
        self.stock_df[f'SMA_{window}'] = self.stock_df['Close'].rolling(window=window).mean()
        return self.stock_df

    def add_rsi(self, window=14):
        """Adds RSI (Relative Strength Index) manually to avoid TA-Lib issues."""
        delta = self.stock_df['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
        rs = gain / loss
        self.stock_df['RSI'] = 100 - (100 / (1 + rs))
        return self.stock_df