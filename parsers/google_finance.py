from bs4 import BeautifulSoup
import requests

def fetch_ticker_details(ticker):
    try:
        ticker_details = ticker.split(":")
        URL = f'https://www.google.com/finance/quote/{ticker}?hl=en'

        page = requests.get(URL, timeout=5)
        soup = BeautifulSoup(page.text, 'html.parser')

        name = soup.find('div', {"role" : "heading", "class": "zzDege"}).text.strip()
        tags = [t.text for t in soup.find_all('span', class_ = "w2tnNd")]
        labels = [t.text for t in soup.find_all('div', class_ = "mfs7Fc")]
        values = [t.text for t in soup.find_all('div', class_ = "P6K39c")]

        data = {
            'name': name,
            'tags': tags,
            'values': [{ 'label': labels[i], 'value': values[i] } for i in range(len(labels))],
            'url': URL,
            'exchange': ticker_details[0],
            'symbol': ticker_details[1],
            'ticker': ticker
        }
        return data
    except Exception as e:
        print(str(e))
        return None
