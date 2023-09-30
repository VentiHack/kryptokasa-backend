import datetime
import requests
from core.api_manager.enums import API_URLS


def fetch_price_from_zonda(ticker: str, amount: float, currency: str):
    trading_pair = f"{ticker}-{currency}"
    API_URL = API_URLS['Zonda']
    try:
        response = requests.get(f"{API_URL}/trading/ticker/{trading_pair}")
        data = response.json()
        return {
            'unit_price': float(data['ticker']['lowestAsk']),
            'asset_price': float(data['ticker']['lowestAsk']) * amount,
            'ticker': ticker,
            'currency': currency,
            'api_url': API_URL,
            'exchange_name': 'Zonda',
            'time': datetime.datetime.now()
        }
    except Exception as e:
        print(e)
        return None


if __name__ == "__main__":
    print(fetch_price_from_zonda('BTC',1, 'PLN'))
