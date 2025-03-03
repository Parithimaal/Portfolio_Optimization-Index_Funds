import numpy as np
import pandas as pd
import yfinance as yf

class Utils:
    @staticmethod
    def fetch_data(tickers, labels, start_date, end_date):
        ticker_label = dict()
        all_prices_df = yf.download(tickers, start=start_date, end=end_date)['Close']
        all_prices_dict = {}
        for ticker, label in zip(tickers, labels):
            all_prices_dict[label] = all_prices_df[[ticker]]
        return all_prices_dict