import pandas

global stock_details_db

STOCK_DETAILS_COLUMNS = ['ticker', 'label', 'value']

stock_details_db = pandas.DataFrame(columns=STOCK_DETAILS_COLUMNS)
