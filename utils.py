import numpy as np
import pandas as pd
import yfinance as yf

class Utils:
    @staticmethod
    def fetch_data(tickers, labels, start_date, end_date):
        ticker_label = dict()
        all_prices_df = yf.download(tickers, start=start_date, end=end_date)['Close']
        all_prices_df = all_prices_df.rename(columns=dict(zip(tickers, labels)))
        all_prices_dict = {}
        for col in all_prices_df.columns:
            all_prices_dict[col] = all_prices_df[[col]]
        return all_prices_dict, all_prices_df
    
    @staticmethod
    def df_sliced_by_date(df, start_date, end_date):
        df_filtered = df[(df.index >= start_date) & (df.index <= end_date)]
        return df_filtered