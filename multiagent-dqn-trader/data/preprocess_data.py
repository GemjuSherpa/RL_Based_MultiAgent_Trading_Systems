import os
import pandas as pd
import ta
from utils.logger import setup_logger

logger = setup_logger("preprocess_logger", "logs/preprocess.log")

RAW_DATA_PATH = "data/raw/"
PROCESSED_DATA_PATH = "data/processed/"

COLUMN_NAMES = ["Date", "Close", "High", "Low", "Open", "Volume"]

def preprocess_file(filename):
    input_path = os.path.join(RAW_DATA_PATH, filename)
    output_path = os.path.join(PROCESSED_DATA_PATH, filename)

    logger.info(f"Reading raw data from {input_path}")

    # Skip the first two metadata rows, then manually assign column names
    df = pd.read_csv(input_path, skiprows=2, header=None, names=COLUMN_NAMES, parse_dates=["Date"])
    df = df.sort_values("Date").dropna()

    logger.info(f"Initial cleaned shape: {df.shape}")

    # Add indicators
    df["SMA_20"] = ta.trend.sma_indicator(df["Close"], window=20)
    df["RSI"] = ta.momentum.rsi(df["Close"], window=14)
    df["Returns"] = df["Close"].pct_change()

    df = df.dropna()
    logger.info(f"Final shape with indicators: {df.shape}")

    # Save
    os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)
    df.to_csv(output_path, index=False)
    logger.info(f"Saved processed data to {output_path}")

if __name__ == "__main__":
    for file in os.listdir(RAW_DATA_PATH):
        if file.endswith(".csv"):
            preprocess_file(file)
