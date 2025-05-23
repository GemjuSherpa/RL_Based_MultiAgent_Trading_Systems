import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils.logger import setup_logger

logger = setup_logger("eda_logger", "logs/eda.log")

PROCESSED_DATA_PATH = "data/processed/"
EDA_OUTPUT_PATH = "eda/reports/"

def run_eda(filename):
    input_path = os.path.join(PROCESSED_DATA_PATH, filename)
    df = pd.read_csv(input_path, parse_dates=["Date"])

    logger.info(f"Loaded data: {filename} | Shape: {df.shape}")

    os.makedirs(EDA_OUTPUT_PATH, exist_ok=True)

    # Price over time
    plt.figure(figsize=(10, 4))
    plt.plot(df["Date"], df["Close"], label="Close Price")
    plt.title("Close Price Over Time")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.grid()
    plt.savefig(os.path.join(EDA_OUTPUT_PATH, f"{filename}_price.png"))
    plt.close()

    # Returns distribution
    plt.figure(figsize=(8, 4))
    sns.histplot(df["Returns"], bins=50, kde=True)
    plt.title("Distribution of Daily Returns")
    plt.xlabel("Returns")
    plt.savefig(os.path.join(EDA_OUTPUT_PATH, f"{filename}_returns.png"))
    plt.close()

    # RSI plot
    plt.figure(figsize=(10, 3))
    plt.plot(df["Date"], df["RSI"], color="purple")
    plt.axhline(70, color="red", linestyle="--")
    plt.axhline(30, color="green", linestyle="--")
    plt.title("RSI Over Time")
    plt.savefig(os.path.join(EDA_OUTPUT_PATH, f"{filename}_rsi.png"))
    plt.close()

    # Correlation heatmap
    plt.figure(figsize=(8, 6))
    corr = df[["Close", "High", "Low", "Open", "Volume", "SMA_20", "RSI", "Returns"]].corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Feature Correlation Heatmap")
    plt.savefig(os.path.join(EDA_OUTPUT_PATH, f"{filename}_correlation.png"))
    plt.close()

    logger.info(f"EDA completed and saved for {filename}")

if __name__ == "__main__":
    for file in os.listdir(PROCESSED_DATA_PATH):
        if file.endswith(".csv"):
            run_eda(file)
