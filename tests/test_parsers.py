from parsers.google_finance import fetch_ticker_details

def test_google_finance():
    # Stock test
    assert fetch_ticker_details("GOOGL:NASDAQ")['name'] == 'Alphabet Inc Class A'
    # ETF test
    assert fetch_ticker_details("URA:NYSEARCA")['name'] == 'Global X Uranium ETF'
