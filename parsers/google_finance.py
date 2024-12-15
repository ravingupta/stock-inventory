from bs4 import BeautifulSoup
import requests

def fetch_ticker_details(ticker):
    try:
        ticker_details = ticker.split(":")
        URL = f'https://www.google.com/finance/quote/{ticker}?hl=en'

        page = requests.get(URL, timeout=5)
        soup = BeautifulSoup(page.text, 'html.parser')

        name = soup.find('div', {"role" : "heading", "class": "zzDege"}).text.strip()
        about = soup.find('div', class_ = "bLLb2d").text.strip().replace("\n", " ").replace("Wikipedia", "")
        price = soup.find('div', class_ = "AHmHk").text.strip().replace("$", "").replace(",", "")
        tags = [t.text for t in soup.find_all('span', class_ = "w2tnNd")]
        labels = [t.text for t in soup.find_all('div', class_ = "mfs7Fc")]
        values = [t.text for t in soup.find_all('div', class_ = "P6K39c")]

        # related = [{ 
        #     "name": t.find('div', class_ = "qIEjSe").text.strip(),
        #     "price": t.find('div', class_ = "Z63m9d").text.strip(),
        #     "symbol": t.find('span', class_ = "lUuFj").text.strip()
        # } for t in soup.find_all('div', class_ = "cJd7w")]
        related = [{ 
            "name": t['data-name'],
            "price": t['data-price'],
            "symbol": t['data-symbol'],
            "exchange": t['data-exchange'],
            "ticker": f"{t['data-symbol']}:{t['data-exchange']}",
            "url": f"https://www.google.com/finance/quote/{t['data-symbol']}:{t['data-exchange']}?hl=en",
            "currency": t['data-currency-code']
        } for t in soup.find_all('div', {"jsname" : "UEIKff"})]

        others = [{ 
            "ticker": t['href'].replace("./quote/", ""),
            "name": t.find('div', class_ = "RwFyvf").text.strip(),
            "price": t.find('div', class_ = "YMlKec").text.replace("$", "").replace(",", ""),
            "symbol": t.find('div', class_ = "COaKTb").text.strip(),
            "exchange": t['href'].replace("./quote/", "").split(":")[1],
            "url": f"https://www.google.com/finance/quote/{t['href'].replace('./quote/', '')}?hl=en",
        } for t in soup.find_all('a', class_ = "tOzDHb")]

        data = {
            'name': name,
            'about': about,
            'tags': tags,
            'price': price,
            'values': [{ 'label': labels[i], 'value': values[i] } for i in range(len(labels))],
            'url': URL,
            'exchange': ticker_details[0],
            'symbol': ticker_details[1],
            'ticker': ticker,
            'related': related,
            'others': others
        }
        return data
    except Exception as e:
        print(str(e))
        return None
