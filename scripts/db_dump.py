import threading
from models.db import stock_db, stock_details_db

def dump_to_csv(df, filename):
    df.to_csv(filename, sep=',', encoding='utf-8', index=False, header=True)

def dump_stocks():
    filename = "dump/stocks.csv"
    thread = threading.Thread(target=dump_to_csv, args=(stock_db,filename))
    thread.start()
    

def dump_stock_details():
    filename = "dump/stocks_details.csv"
    thread = threading.Thread(target=dump_to_csv, args=(stock_details_db,filename))
    thread.start()
