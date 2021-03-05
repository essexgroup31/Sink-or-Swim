import numpy
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go

data = yf.download(tickers='BTC-GBP', period='5d', interval='5m')

print(data)