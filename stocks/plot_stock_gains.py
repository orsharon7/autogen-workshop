# filename: plot_stock_gains.py

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Step 1: Fetch the current date
today = datetime.today().strftime('%Y-%m-%d')

# Step 2: Retrieve or scrape the stock price data of top 10 tech stocks
# List of top 10 tech stocks (updated FB to META)
tech_stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'TSLA', 'NVDA', 'NFLX', 'ADBE', 'INTC']

# Fetch YTD data
data = yf.download(tech_stocks, start='2023-01-01', end=today)['Adj Close']

# Step 3: Calculate the YTD gains
ytd_gains = ((data.iloc[-1] - data.iloc[0]) / data.iloc[0]) * 100
ytd_gains = ytd_gains.sort_values(ascending=False)

# Step 4: Create a bar plot to visualize the gains
plt.figure(figsize=(12, 6))
plt.bar(ytd_gains.index, ytd_gains, color='skyblue')
plt.xlabel('Tech Stocks')
plt.ylabel('YTD Gain (%)')
plt.title('Top 10 Tech Stocks YTD Gains')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.xticks(rotation=45)
plt.tight_layout()

# Step 5: Save the plot to a file
plt.savefig('stock_gains.png')
plt.show()

# Output the file name for the user's confirmation
print('The plot has been saved to stock_gains.png')