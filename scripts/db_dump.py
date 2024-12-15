from models.db import stock_db, stock_details_db

def dump_stocks():
    print(stock_db)
    stock_db.to_csv("dump/stocks.csv", sep=',', encoding='utf-8', index=False, header=True)

def dump_stock_details():
    print(stock_details_db)
    stock_details_db.to_csv("dump/stocks_details.csv", sep=',', encoding='utf-8', index=False, header=True)
