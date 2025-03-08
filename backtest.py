import numpy as np
import pandas as pd

class Backtesting():
    def __init__(self, assets):
        self.transaction_dict = {
            asset: pd.DataFrame(columns=['units', 'unit_price', 'value'])
            for asset in assets
        }

    def sell_and_calc_pf_val(self, current_unit_price_dict, date: str, investment_amount, optimal_weights_dict):
        portfolio_value = 0
        for asset in current_unit_price_dict.keys():
            df = self.transaction_dict[asset]
            if not df.empty:            
                # current value = previous units sold at current price
                current_value = df['units'].iloc[-1] * current_unit_price_dict[asset]
                portfolio_value += current_value
        return portfolio_value
            
            
    def buy(self, current_unit_price_dict, date: str, investment_amount, optimal_weights_dict):
        for asset in current_unit_price_dict.keys():
            unit_price = current_unit_price_dict[asset]
            value = optimal_weights_dict[asset]*investment_amount
            units = value / unit_price

            row=pd.Series({'units':units, 'unit_price':unit_price, 'value':value}, name=date)
            self.transaction_dict[asset].loc[date] = [units, unit_price, value]
    
    def get_transaction_dict(self):
        return self.transaction_dict
            


            
            
        
        
        