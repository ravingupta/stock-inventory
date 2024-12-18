import os

DUMP_DIR = "dump"
STOCK_DETAILS_FILE = os.path.join(DUMP_DIR, "stocks_details.csv")
STOCKS_FILE = os.path.join(DUMP_DIR, "stocks.csv")

STOCK_COLUMNS = ['name', 'tags', 'url', 'exchange', 'symbol', 'ticker', 'price', 'about', 'last_modified']
STOCK_DETAILS_COLUMNS = ['ticker', 'label', 'value']