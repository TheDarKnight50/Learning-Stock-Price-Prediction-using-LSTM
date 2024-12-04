# Stock Data Analysis Assignment
# Objective: Fetch stock data using yfinance and analyze it using pandas.

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def fetch_stock_data(ticker, start_date, end_date):
    """
    Fetch historical stock data for the given ticker and date range.
    
    Args:
        ticker (str): Stock ticker symbol (e.g., "AAPL").
        start_date (str): Start date in 'YYYY-MM-DD' format.
        end_date (str): End date in 'YYYY-MM-DD' format.
    
    Returns:
        pd.DataFrame: DataFrame containing the stock data.
    """
    # TODO: Use yfinance to download stock data for the specified ticker and date range.
    # Hint: Use yf.download() and specify the ticker, start_date, and end_date.
    # Remove the 'raise' statement once implemented.
    raise NotImplementedError("You need to fetch stock data using yfinance.")

def clean_data(data):
    """
    Clean the stock data by handling missing values.
    
    Args:
        data (pd.DataFrame): DataFrame with raw stock data.
    
    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    # TODO: Handle missing values in the DataFrame.
    # Hint: Use forward-fill or backward-fill to handle NaN values.
    # Remove the 'raise' statement once implemented.
    raise NotImplementedError("You need to clean the data by handling missing values.")

def calculate_descriptive_stats(data):
    """
    Calculate descriptive statistics like average, max, and min closing price.
    
    Args:
        data (pd.DataFrame): DataFrame with stock data.
    
    Returns:
        dict: Dictionary with average, max, min, and corresponding dates.
    """
    # TODO: Calculate the following:
    # - Average closing price
    # - Maximum closing price and its date
    # - Minimum closing price and its date
    # Hint: Use pandas methods like .mean(), .max(), and .idxmax().
    # Remove the 'raise' statement once implemented.
    raise NotImplementedError("You need to calculate descriptive statistics.")

def compute_rolling_averages(data, window_sizes):
    """
    Compute rolling averages for the given window sizes.
    
    Args:
        data (pd.DataFrame): DataFrame with stock data.
        window_sizes (list): List of integers representing window sizes (e.g., [20, 50]).
    
    Returns:
        pd.DataFrame: DataFrame with rolling averages added as columns.
    """
    # TODO: Compute rolling averages for each window size and add them as new columns.
    # Hint: Use pandas' .rolling() method followed by .mean().
    # Remove the 'raise' statement once implemented.
    raise NotImplementedError("You need to compute rolling averages.")

def compute_daily_returns(data):
    """
    Compute daily returns for the stock data.
    
    Args:
        data (pd.DataFrame): DataFrame with stock data.
    
    Returns:
        pd.DataFrame: DataFrame with daily returns added as a column.
    """
    # TODO: Compute daily percentage returns based on the 'Close' column.
    # Hint: Daily returns can be calculated as (current_close - previous_close) / previous_close.
    # Remove the 'raise' statement once implemented.
    raise NotImplementedError("You need to compute daily returns.")

def plot_stock_data(data, ticker):
    """
    Plot the stock's closing price and rolling averages over time.
    
    Args:
        data (pd.DataFrame): DataFrame with stock data and rolling averages.
        ticker (str): Stock ticker symbol.
    """
    # TODO: Plot the closing price and rolling averages.
    # Hint: Use matplotlib to create the plot. Ensure proper labels and a legend.
    # Remove the 'raise' statement once implemented.
    raise NotImplementedError("You need to plot the closing price and rolling averages.")

def save_to_csv(data, filename):
    """
    Save the processed DataFrame to a CSV file.
    
    Args:
        data (pd.DataFrame): DataFrame to save.
        filename (str): Name of the CSV file.
    """
    # TODO: Save the DataFrame to a CSV file.
    # Hint: Use pandas' .to_csv() method.
    # Remove the 'raise' statement once implemented.
    raise NotImplementedError("You need to save the processed data to a CSV file.")

# Main function to orchestrate the tasks
if __name__ == "__main__":
    print("Welcome to the Stock Data Analysis Assignment!")
    
    # TODO: Ask the user for stock ticker, start date, and end date.
    ticker = input("Enter the stock ticker symbol (e.g., AAPL): ")
    start_date = "2022-01-01"  # Fixed start date for simplicity
    end_date = "2023-01-01"    # Fixed end date for simplicity
    
    # Fetch stock data
    print("Fetching stock data...")
    data = fetch_stock_data(ticker, start_date, end_date)
    
    # Clean the data
    print("Cleaning data...")
    data = clean_data(data)
    
    # Calculate descriptive statistics
    print("Calculating descriptive statistics...")
    stats = calculate_descriptive_stats(data)
    print("Descriptive Statistics:", stats)
    
    # Compute rolling averages
    print("Computing rolling averages...")
    data = compute_rolling_averages(data, window_sizes=[20, 50])
    
    # Compute daily returns
    print("Computing daily returns...")
    data = compute_daily_returns(data)
    
    # Plot the stock data
    print("Plotting stock data...")
    plot_stock_data(data, ticker)
    
    # Save the processed data to a CSV file
    print("Saving processed data to CSV...")
    save_to_csv(data, f"{ticker}_processed_data.csv")
    
    print("Assignment complete! Check your CSV file and plots.")
