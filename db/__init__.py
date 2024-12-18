import os
import pandas as pd

from constants import DUMP_DIR, STOCKS_FILE, STOCK_DETAILS_FILE, STOCK_COLUMNS, STOCK_DETAILS_COLUMNS

if not os.path.exists(DUMP_DIR):
    os.makedirs(DUMP_DIR)

stock_db = pd.read_csv(STOCKS_FILE) if os.path.isfile(STOCKS_FILE) else pd.DataFrame(columns=STOCK_COLUMNS)
stock_details_db = pd.read_csv(STOCK_DETAILS_FILE) if os.path.isfile(STOCK_DETAILS_FILE) else pd.DataFrame(columns=STOCK_DETAILS_COLUMNS)