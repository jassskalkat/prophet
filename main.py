
# Prophet is a price forecasting tool that renders the model of an asset with its predicted price.
# The program uses open-source libraries and can be called directly from the command line.

# libraries needed for the model 
import argparse
import yfinance as yf
from prophet import Prophet
import matplotlib.pyplot as plt

# reading and parsing the command line arguments
parser = argparse.ArgumentParser(description="Facebook Prophet")
parser.add_argument("--ticker", type=str, help="stock ticker or crypto ticker")
parser.add_argument("--date", type=str, help="start date for prediction")
parser.add_argument("--days", type=int, help="days in future for prediction")
args = parser.parse_args()

# storing the parsed to variables to simplify operations
ticker = args.ticker
date = args.date
days = args.days


# function for prediction based of the parameters
def prediction(ticker, date, days):
    df = yf.download(ticker, start=date)
    df = df.reset_index()
    df[['ds', 'y']] = df[['Date', 'Adj Close']]
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(days)
    forecast = model.predict(future)
    model.plot(forecast)
    plt.show()


# invoking the function with the arguments
prediction(ticker, date, days)
