import numpy as np
import pandas as pd
import plotly.express as px

class FinancialMetrics:
    def __init__(self, risk_free_rate):
        self.risk_free_rate = risk_free_rate
        print(self.risk_free_rate)

    @staticmethod
    def _get_values(df, years):
        """
        Helper function to filter the DataFrame and get start & end values.
        """
        end_date = df.index.max()
        start_date = end_date - pd.DateOffset(years=years)
        
        df_filtered = df[df.index >= start_date]
        if df_filtered.empty:
            raise ValueError(f"Not enough data available for {years} years.")

        value_begin = df_filtered.iloc[0, 0]
        value_end = df_filtered.iloc[-1, 0]

        return value_begin, value_end

    def calculate_sharpe_ratio(self, prices_df):
        """
        Calculates the Sharpe Ratio for a given set of index fund closing prices.

        Parameters:
        -prices_df(pd.DataFrame): The dataframe containing the closing price of instrument
        -risk_free_rate(float): The return (percent) of a baseline risk free investment instrument

        Returns:
        -Annualized sharpie ratio as a dictionary
        """
        # Daily returns
        daily_returns = prices_df.pct_change().dropna()
        
        # Converting risk-free rate to daily (assuming 252 trading days)
        daily_risk_free_rate = (1 + self.risk_free_rate)**(1/252) - 1
        
        # Excess returns
        excess_returns = daily_returns - daily_risk_free_rate
        
        sharpe_ratios = excess_returns.mean() / excess_returns.std()
        annualized_sharpe = sharpe_ratios * np.sqrt(252)
        
        return annualized_sharpe.iloc[0]
    
    @staticmethod
    def plot_cumulative_returns(prices_df):
        """
        Calculates the cumulative returns of the given data frame
        """
        # Calculate daily percentage change
        df_normalized = prices_df.pct_change().dropna()  
        # Convert to cumulative return (starting at 1)
        df_cumulative = (1 + df_normalized).cumprod()  
        fig = px.line(df_cumulative, x=df_cumulative.index, y=df_cumulative.columns,
                  labels={"value": "Cumulative Return", "index": "Date"})
        return fig
        
    @staticmethod    
    def plot_cumulative_returns_multi(dfs, labels, title="Normalized Percentage Change of Multiple Assets"):
        """
        Plots normalized percentage change for multiple dataframes using the first column.
    
        Parameters:
        - dfs (list of pd.DataFrame): Multiple DataFrames with date index and price columns.
        - labels (list): List of names corresponding to each DataFrame.
        - title (str): Title of the plot.
    
        Returns:
        - A Plotly line chart showing normalized percentage change for all assets.
        """
        normalized_dfs = []
    
        # Normalize each DataFrame separately
        for df, label in zip(dfs, labels):
            df = df.iloc[:, 0].pct_change().dropna()  # Use the first column (positional reference)
            df = (1 + df).cumprod() * 100  # Normalize: Start each asset at 100
            df = df.to_frame(name=label)  # Convert Series to DataFrame and rename column
            normalized_dfs.append(df)
    
        # Combine all DataFrames into one
        df_combined = pd.concat(normalized_dfs, axis=1)
    
        # Plot the combined DataFrame
        fig = px.line(df_combined, x=df_combined.index, y=df_combined.columns,
                      title=title, labels={"value": "Cumulative Return (Starting at 100)", "index": "Date"})
        
        fig.show()
        
    @staticmethod
    def calculate_cagr(df, years=1): #period is specified in number of years
        value_begin, value_end = FinancialMetrics._get_values(df, years)
        cagr = (value_end/value_begin)**(1/years) - 1
        return round(cagr,6)
        
    @staticmethod    
    def calculate_returns(df, years=1): #period is specified in number of years
        value_begin, value_end = FinancialMetrics._get_values(df, years)
        return_in_period = (value_end/value_begin) -1
        return round(return_in_period,6)