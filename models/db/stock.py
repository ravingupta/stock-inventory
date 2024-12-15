import os
import pandas

global stock_db

STOCK_COLUMNS = ["name", "tags", "url", "exchange", "symbol", "ticker", "price", "about", "last_modified"]

if os.path.isfile("dump/stocks.csv"):
    stock_db = pandas.read_csv("dump/stocks.csv")
else:
    stock_db = pandas.DataFrame(columns=STOCK_COLUMNS)
