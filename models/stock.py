import threading
from datetime import datetime
import pandas as pd

from db import stock_db, stock_details_db
from constants import STOCK_DETAILS_COLUMNS, STOCK_COLUMNS
from scripts.db_dump import dump_stocks, dump_stock_details

lock = threading.Lock()

class StockDetails:
    def __init__(self, ticker, data):
        self.ticker = ticker
        self.label = data.get('label')
        self.value = data.get('value')

    def save(self):
        global stock_details_db
        with lock:
            # Check if the record already exists
            existing = StockDetails.filter({'ticker': self.ticker, 'label': self.label})
            if not existing.empty:
                stock_details_db.loc[existing.index, 'value'] = self.value
            else:
                stock_details_db = pd.concat([
                    stock_details_db,
                    pd.DataFrame([[self.ticker, self.label, self.value]], columns=STOCK_DETAILS_COLUMNS)
                ], ignore_index=True)
        dump_stock_details()
        return self

    @staticmethod
    def filter(data):
        filtered_df = stock_details_db
        for key, value in data.items():
            if key in STOCK_DETAILS_COLUMNS:
                filtered_df = filtered_df[filtered_df[key] == value]
            else:
                raise ValueError(f"Invalid filter key: {key}")
        return filtered_df

    @staticmethod
    def unique(column):
        if column in STOCK_DETAILS_COLUMNS:
            return stock_details_db[column].unique()
        raise ValueError(f"Invalid column: {column}")

    @staticmethod
    def objects():
        return stock_details_db

class Stock:
    def __init__(self, data):
        self.name = data.get('name')
        self.tags = data.get('tags', [])
        self.url = data.get('url')
        self.exchange = data.get('exchange')
        self.symbol = data.get('symbol')
        self.ticker = data.get('ticker')
        self.price = data.get('price')
        self.about = data.get('about')
        self.last_modified = datetime.now()
        self.values = [StockDetails(self.ticker, t) for t in data.get('values', [])]

        # Create entry for all related drugs
        for t in data.get('related', []):
            Stock(t).save()
        for t in data.get('others', []):
            Stock(t).save()

    def save(self):
        global stock_db
        with lock:
            # Check if the stock exists
            existing = Stock.filter({'ticker': self.ticker})
            if not existing.empty:
                stock_db.loc[existing.index, ['price', 'about', 'last_modified']] = [
                    self.price, self.about, self.last_modified
                ]
            else:
                stock_db = pd.concat([
                    stock_db,
                    pd.DataFrame([[
                        self.name, self.tags, self.url, self.exchange, self.symbol,
                        self.ticker, self.price, self.about, self.last_modified
                    ]], columns=STOCK_COLUMNS)
                ], ignore_index=True)
        dump_stocks()

        # Save stock details
        for value in self.values:
            value.save()
        return self

    @staticmethod
    def filter(data):
        filtered_df = stock_db
        for key, value in data.items():
            if key in STOCK_COLUMNS:
                filtered_df = filtered_df[filtered_df[key] == value]
            else:
                raise ValueError(f"Invalid filter key: {key}")
        return filtered_df

    @staticmethod
    def unique(column):
        if column in STOCK_COLUMNS:
            return stock_db[column].unique()
        raise ValueError(f"Invalid column: {column}")

    @staticmethod
    def objects():
        return stock_db