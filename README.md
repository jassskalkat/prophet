# prophet
We all want an easy life, and no doubt investing can give you that life and make you rich if you play your cards right. 
But there are always suspicions when it comes to investing. It's hard to choose assets that return lucrative profits. 
This program can help you select the right asset by predicting its future price using the open-source library 'fbprophet' etc.

Requirements to run the script:

1. pystan library
2. prophet library
3. yfinance library

If you dont have these libraries installed you can create a venv (virtual enviroment) to run the program.
Follow the steps below to create a venv:

1. Open the terminal
2. Go to the same directory as 'prophet'
3. type the command: python -m venv venv
4. type the command: source venv/bin/activate
5. type the command: pip install pystan==2.19.1.1 prophet yfinance

How to use the script to predict the price of an asset?

The script takes three arguments and can be called directly from the command-line.
1. --ticker
2. --date
3. --days

Go to the same directory as 'prophet' and run the following command in a venv terminal to get comfortable with running the script.
python main.py --ticker BTC-USD --date 2015-01-01 --days 365
