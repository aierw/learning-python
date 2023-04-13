from datetime import datetime
import yfinance as yf
#import matplotlib.pyplot as plt

# initialize parameters
start_date = datetime(2018, 1, 1)
end_date = datetime(2021, 1, 1)
  
# get the data
data = yf.download('BTC-USD', start = start_date,
                   end = end_date)

data.to_csv('C:\Users\User\Documents\GitHub\learning-python\wow\GOOGL.csv', index=False) 

# plot data

dates = data['Date']
closing_prices = data['Close']

#plt.plot_date(dates, closing_prices)
