# download_data.py
import yfinance as yf
import os
import sys
import pandas as pd
from datetime import datetime
import logging

from utils.logger import setup_logger


# Setup logging
log_file_path = "logs/logs.log"
logger = setup_logger("logs.log", log_file_path)

logger.info("Logger initialized for download_data")


def download_price_data(ticker: str, start_date: str, end_date: str, interval: str = "1h"):
    """
    Download historical price data using yfinance.
    :param ticker: Symbol (e.g., 'AAPL', 'BTC-USD', 'EURUSD=X')
    :param start_date: Start date in 'YYYY-MM-DD'
    :param end_date: End date in 'YYYY-MM-DD'
    :param interval: Data interval (e.g., '1m', '5m', '1h', '1d', '1wk', '1mo')
    :return: None (saves data to CSV)
    """
    logger.info(f"Fetching data for {ticker} from {start_date} to {end_date} with interval '{interval}'")

    try:
        data = yf.download(ticker, start=start_date, end=end_date, interval=interval)
        if data.empty:
            logger.warning(f"No data found for {ticker}")
            return

        # Ensure output directory exists
        os.makedirs("data/raw", exist_ok=True)
        filename = f"data/raw/{ticker.replace('=', '_')}_{start_date}_to_{end_date}_{interval}.csv"
        data.to_csv(filename)
        logger.info(f"Saved data to {filename}")

    except Exception as e:
        logger.error(f"Error downloading data for {ticker}: {e}")

# Example usage
if __name__ == "__main__":
    download_price_data("BTC-USD", "2024-01-01", "2025-04-30", interval="1h")
    download_price_data("AAPL", "2022-01-01", "2022-12-31", interval="1d")
    download_price_data("EURUSD=X", "2022-01-01", "2022-12-31", interval="1d")
