import threading

from db import stock_db, stock_details_db
from constants import STOCKS_FILE, STOCK_DETAILS_FILE

lock = threading.Lock()

def dump_to_csv(df, filename):
    with lock:
        df.to_csv(filename, sep=',', encoding='utf-8', index=False, header=True)

def dump_stocks():
    dump_to_csv(stock_db, STOCKS_FILE)

def dump_stock_details():
    dump_to_csv(stock_details_db, STOCK_DETAILS_FILE)
