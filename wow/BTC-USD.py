import yfinance as yf
from datetime import datetime
import csv

# Define the ticker symbol
tickerSymbol = 'BTC-USD'

# Set the start and end dates
start_date = datetime(2022, 1, 1)
end_date = datetime(2023, 4, 10)

# Get data on the ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start=start_date, end=end_date)

# Save the data to a CSV file
with open('BTC-USD.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(tickerDf.values)


#dates = tickerDf['Date']
#closing_prices = tickerDf['Close']

