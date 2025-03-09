# Portfolio_Optimization-Index_Funds

## Introduction
This repository demonstrates a simple approach to portfolio optimization using historical data from multiple index funds and ETFs. It uses Mean-Variance Optimization (MVO) principles to construct an efficient portfolio that minimizes total portfolio variance for a target return subject to constraints like minimum investment amounts, transaction costs, target returns, etc. The project leverages Pyomo and a solver (Gurobi) to solve the optimization problems, and uses yFinance for retrieving historical data.

## Table of Contents
1. [Project Structure](#project-structure)  
2. [Key Dependencies](#key-dependencies)  
3. [Setup and Usage](#setup-and-usage)  
4. [How It Works](#how-it-works)  
5. [Backtesting](#backtesting)  
6. [Future Enhancements](#future-enhancements)  
7. [Disclaimer](#disclaimer)

## Project Structure

### Files Description

1. **Main.ipynb**  
   - Orchestrates fetching data, building the optimization model, running backtests, and compiling results.

2. **backtest.py**  
   - Contains a `Backtesting` class responsible for simulating buy and sell transactions over time.
   - Helps in computing the final portfolio value after successive rebalances.

3. **financial_analysis.py**  
   - Defines a `FinancialMetrics` class for calculating:
     - Sharpe Ratio
     - Cumulative returns
     - CAGR (Compound Annual Growth Rate)
     - Covariance matrices
     - Other financial performance metrics
   - Includes plotting methods (Plotly) for visualizing portfolio performance and comparisons.

4. **utils.py**  
   - A `Utils` class providing helper methods:
     - `fetch_data`: Fetches historical price data from Yahoo Finance.
     - `df_sliced_by_date`: Slices DataFrame by a specified date range.

5. **Gurobi_log.txt** (Optional)  
   - Stores solver logs if desired, capturing progress and status of optimization runs.

## Key Dependencies
Below are the primary Python libraries and tools used in this project. Make sure to have them installed before running the code:
- **NumPy**  
- **Pandas**  
- **yFinance**  
- **Pyomo**  
- **Gurobi** (or another solver compatible with Pyomo)  
- **plotly**  
- **datetime, dateutil**  

You can install most Python dependencies via:
**Note**: Gurobi is a commercial solver. You may need a license or to use a community edition (if available).

## Setup and Usage

1. **Clone the repository**:
git clone https://github.com/Parithimaal/Portfolio_Optimization-Index_Funds.git

2. **Install dependencies**:
pip install -r requirements.txt
or install them individually as indicated above.

3. **Open the Jupyter notebook**:
jupyter notebook Main.ipynb

4. **Run the notebook cells**:
- This will fetch historical price data using `yFinance`.
- Build and solve the optimization model using Pyomo and Gurobi.
- Perform backtesting to verify portfolio performance over time.

## How It Works

1. **Data Fetching**  
- `utils.py` uses yFinance to download closing prices for multiple tickers over the specified date range.
2. **Financial Analysis**  
- `financial_analysis.py` computes key metrics such as returns, CAGR, covariance, etc.
3. **Optimization Model**  
- `Main.ipynb` defines and solves a Mean–Variance optimization model:
  - **Objective**: Minimize portfolio variance (risk).
  - **Constraints**:
    - Portfolio weights sum to 1.
    - Return target must be met.
    - Transaction costs and minimum investment amounts.
4. **Solver**  
- Uses Gurobi by default, but can be switched to any Pyomo-supported solver that supports both MILP and continuous system optimization.
5. **Backtesting**  
- `backtest.py` simulates the portfolio over multiple time periods, recalculating optimal allocations each year (or at a chosen interval).

## Backtesting
- The `Backtesting` class in `backtest.py`:
- **sell_and_calc_pf_val**: Calculates the portfolio value upon selling existing positions at current prices.
- **buy**: Buys assets according to newly computed optimal weights.
- Tracks and updates a transaction dictionary that contains unit prices, units purchased, and total value.

## Future Enhancements
- Implement multiple optimization strategies (e.g., maximizing Sharpe Ratio).
- Add user-friendly CLI or web interface.
- Integrate advanced techniques (e.g., Black-Litterman model, Monte Carlo Simulation).

## Disclaimer
This repository is for **educational purposes only**. It demonstrates the basics of portfolio optimization and backtesting. **No information here constitutes financial advice**, and real-world investments involve many additional complexities. Use at your own risk.


