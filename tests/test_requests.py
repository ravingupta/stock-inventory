import pytest
from flask import Flask
from unittest.mock import patch
import pandas as pd

from parsers.google_finance import fetch_ticker_details
from src import stocks_view
from models import Stock


# Test data
TEST_STOCKS_DATA = [
    {
        "name": "Alphabet Inc Class A",
        "ticker": "GOOGL:NASDAQ",
        "url": "https://www.google.com/finance/quote/GOOGL:NASDAQ?hl=en"
    }
]

TEST_STOCK_DETAILS = [
    {"ticker": "GOOGL:NASDAQ", "label": "Market Cap", "value": "1.8T"}
]

# Create a test Flask app
@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(stocks_view)
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Mock CSV data setup
@pytest.fixture
def setup_test_data():
    global stock_db, stock_details_db
    stock_db = pd.DataFrame(TEST_STOCKS_DATA)
    stock_details_db = pd.DataFrame(TEST_STOCK_DETAILS)
    yield
    # Cleanup after tests
    stock_db = pd.DataFrame()
    stock_details_db = pd.DataFrame()

# Test /stocks endpoint
def test_all_stocks_get(client, setup_test_data):
    response = client.get('/stocks')
    assert response.status_code == 200
    assert b"Google" in response.data  # Verify stock name in rendered HTML

def test_all_stocks_post(client, setup_test_data):
    with patch('parsers.fetch_ticker_details', return_value=TEST_STOCKS_DATA[0]):
        response = client.post('/stocks', json={"ticker": "GOOGL:NASDAQ"})
        assert response.status_code == 200
        assert b"Success" in response.data

def test_all_stocks_post_duplicate(client, setup_test_data):
    response = client.post('/stocks', json={"ticker": "GOOGL:NASDAQ"})
    assert response.status_code == 200
    assert b"Stock already exist" in response.data

# Test /stock/<stock> endpoint
def test_stock_details(client, setup_test_data):
    response = client.get('/stock/GOOGL:NASDAQ')
    assert response.status_code == 200

# Test model methods
def test_stock_save():
    stock = Stock(TEST_STOCKS_DATA[0])
    stock.save()
    assert len(stock_db) == 1
    assert stock_db.iloc[0]['name'] == "Google"

def test_stock_filter():
    stock = Stock(TEST_STOCKS_DATA[0])
    stock.save()
    filtered = Stock.filter({"ticker": "GOOGL:NASDAQ"})
    assert not filtered.empty
    assert filtered.iloc[0]['name'] == "Google"

def test_stock_unique():
    stock = Stock(TEST_STOCKS_DATA[0])
    stock.save()
    unique_tickers = Stock.unique("ticker")
    assert len(unique_tickers) == 1
    assert unique_tickers[0] == "GOOGL:NASDAQ"

# Test fetch_ticker_details
def test_fetch_ticker_details():
    with patch('requests.get') as mock_get:
        mock_get.return_value = """
        <div role="heading" class="zzDege">Alphabet Inc Class A</div>
        """
        data = fetch_ticker_details("GOOGL:NASDAQ")
        assert data['name'] == "Alphabet Inc Class A"
