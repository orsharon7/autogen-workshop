# filename: stock_price_plot.py

import subprocess
import sys

# Function to install packages
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install yfinance and matplotlib if they're not already installed
try:
    import yfinance as yf
except ImportError:
    install('yfinance')
    import yfinance as yf

try:
    import matplotlib.pyplot as plt
except ImportError:
    install('matplotlib')
    import matplotlib.pyplot as plt

from datetime import datetime

# Define the tickers
tickers = ["NVDA", "TSLA"]

# Fetch the current year
current_year = datetime.now().year

# Fetching the historical data for YTD
data = yf.download(tickers, start=f'{current_year}-01-01', end=datetime.now().strftime("%Y-%m-%d"))

# Calculate the YTD percentage change
nvda_pct_change = data['Adj Close']['NVDA'].pct_change().add(1).cumprod().sub(1).mul(100)
tesla_pct_change = data['Adj Close']['TSLA'].pct_change().add(1).cumprod().sub(1).mul(100)

# Plotting the data
plt.figure(figsize=(14, 7))
plt.plot(nvda_pct_change.index, nvda_pct_change.values, label="NVDA YTD % Change")
plt.plot(tesla_pct_change.index, tesla_pct_change.values, label="TSLA YTD % Change")
plt.title("NVDA vs TSLA Stock Price Percentage Change YTD")
plt.xlabel("Date")
plt.ylabel("Percentage Change")
plt.legend()
plt.grid(True)
plt.show()