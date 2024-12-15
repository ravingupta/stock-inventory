import os
import pandas

global stock_details_db

STOCK_DETAILS_COLUMNS = ['ticker', 'label', 'value']

if os.path.isfile("dump/stocks.csv"):
    stock_details_db = pandas.read_csv("dump/stocks_details.csv")
else:
    stock_details_db = pandas.DataFrame(columns=STOCK_DETAILS_COLUMNS)
