from .db import stock_db, stock_details_db, STOCK_DETAILS_COLUMNS, STOCK_COLUMNS

class StockDetails:
    ticker = None
    label = None
    value = None

    def __init__(self, ticker, data):
        self.ticker = ticker
        self.label = data['label']
        self.value = data['value']

    def save(self):
        obj = StockDetails.filter({'ticker': self.ticker, 'label': self.label})
        if not obj.empty:
            obj[0]['value'] = self.value
        else:
            stock_details_db.loc[len(stock_details_db)] = [self.ticker, self.label, self.value]
        return self

    @staticmethod
    def filter(data):
        filtered_df = stock_details_db
        for key in data.keys():
            if key in STOCK_DETAILS_COLUMNS:
                filtered_df = filtered_df[filtered_df[key] == data[key]]
            else:
                raise Exception(f"Filter '{key}' doesn't exist")
        return filtered_df
    
    @staticmethod
    def unique(col):
        if col in STOCK_DETAILS_COLUMNS:
            return stock_details_db[col].unique()
        raise Exception(f"Column '{col}' doesn't exist")

class Stock:
    name = None
    tags = []
    url = None
    exchange = None
    symbol = None
    ticker = None
    values = []

    def __init__(self, data):
        self.name = data['name']
        self.tags = data['tags']
        self.url = data['url']
        self.exchange = data['exchange']
        self.symbol = data['symbol']
        self.ticker = data['ticker']
        self.values = [StockDetails(self.ticker, t) for t in data['values']]

    def save(self):
        obj = Stock.filter({'ticker': self.ticker})
        if not obj.empty:
            stock_db.loc[stock_db['ticker'] == self.ticker, "name"] = self.name
            stock_db.loc[stock_db['ticker'] == self.ticker, "url"] = self.url
            stock_db.loc[stock_db['ticker'] == self.ticker, "exchange"] = self.exchange
            stock_db.loc[stock_db['ticker'] == self.ticker, "symbol"] = self.symbol
        else:
            stock_db.loc[len(stock_db)] = [self.name, self.tags, self.url, self.exchange, self.symbol, self.ticker]
        return self

    @staticmethod
    def filter(data):
        filtered_df = stock_db
        for key in data.keys():
            if key in STOCK_COLUMNS:
                filtered_df = filtered_df[filtered_df[key] == data[key]]
            else:
                raise Exception(f"Filter '{key}' doesn't exist")
        return filtered_df

    @staticmethod
    def unique(col):
        if col in STOCK_COLUMNS:
            return stock_db[col].unique()
        raise Exception(f"Column '{col}' doesn't exist")
