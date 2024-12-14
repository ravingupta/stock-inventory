import pandas

global stock_db

STOCK_COLUMNS = ["name", "tags", "url", "exchange", "symbol", "ticker"]

stock_db = pandas.DataFrame(columns=STOCK_COLUMNS)
