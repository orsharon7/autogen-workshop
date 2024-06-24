# filename: plot_stock_prices.py
import yfinance as yf
import matplotlib.pyplot as plt
import datetime

# Define the tickers and start date
tickers = ['NVDA', 'TSLA']
start_date = datetime.date.today().replace(month=1, day=1).strftime('%Y-%m-%d')
end_date = datetime.date.today().strftime('%Y-%m-%d')

# Fetch the stock data
nvda = yf.download('NVDA', start=start_date, end=end_date)
tsla = yf.download('TSLA', start=start_date, end=end_date)

# Plot the adjusted close price YTD
plt.figure(figsize=(14, 7))
plt.plot(nvda['Adj Close'], label='NVDA')
plt.plot(tsla['Adj Close'], label='TSLA')
plt.title('NVDA and TSLA Stock Price Change YTD')
plt.xlabel('Date')
plt.ylabel('Adjusted Close Price (USD)')
plt.legend()
plt.grid(True)
plt.show()