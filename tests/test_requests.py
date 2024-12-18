import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from app import stocks_view  # Import the blueprint from your app

@pytest.fixture
def client():
    """Fixture for creating a Flask test client."""
    app = Flask(__name__)
    app.register_blueprint(stocks_view)
    app.config['TESTING'] = True
    client = app.test_client()
    yield client


@patch('app.stocks_view')
def test_all_stocks_get(mock_stocks_view, client):
    """Test GET request for /stocks route."""
    mock_stocks_view.return_value.to_json.return_value = '[{"ticker": "AAPL", "price": 150}]'
    response = client.get('/stocks')
    assert response.status_code == 200
    assert b"AAPL" in response.data


# @patch('models.Stock.filter')
# @patch('parsers.fetch_ticker_details')
# @patch('models.Stock.save')
# def test_all_stocks_post(mock_save, mock_fetch_ticker_details, mock_filter, client):
#     """Test POST request for /stocks route."""
#     # Simulate an empty filter result and a valid fetch result
#     mock_filter.return_value.empty = True
#     mock_fetch_ticker_details.return_value = {"ticker": "AAPL", "price": 150}

#     response = client.post('/stocks', json={"ticker": "AAPL"})
#     assert response.status_code == 200
#     assert b"Success" in response.data

#     # Test when stock already exists
#     mock_filter.return_value.empty = False
#     response = client.post('/stocks', json={"ticker": "AAPL"})
#     assert b"Stock already exist" in response.data

#     # Test failure case
#     response = client.post('/stocks', json={})
#     assert b"Request Failed" in response.data


# @patch('models.stock_details_db.dump_to_csv')
# def test_dump_stock_details(mock_dump_to_csv):
#     """Test dump_stock_details functionality."""
#     from scripts import dump_stock_details
#     from models.db import stock_details_db
#     dump_stock_details()
#     mock_dump_to_csv.assert_called_once_with(stock_details_db, "dump/stocks_details.csv")


# @patch('app.requests.get')
# def test_fetch_ticker_details(mock_beautifulsoup, mock_requests_get):
#     """Test fetch_ticker_details function."""
#     from parsers import fetch_ticker_details
#     ticker = "AAPL:NASDAQ"
#     result = fetch_ticker_details(ticker)
#     assert result is not None
#     assert result['ticker'] == ticker
