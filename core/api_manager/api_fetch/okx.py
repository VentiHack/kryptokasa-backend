import datetime
import requests
from core.api_manager.enums import API_URLS


# now binance fetching is mocked, we multiply zonda price * 0.9, just for price difference simulation
def fetch_price_from_okx(ticker: str, amount: float, currency: str):
    trading_pair = f"{ticker}-{currency}"
    API_URL = API_URLS['Zonda']
    try:
        response = requests.get(f"{API_URL}/trading/ticker/{trading_pair}")
        data = response.json()
        return {
            'unit_price': float(data['ticker']['lowestAsk']) * 1.15,
            'asset_price': float(data['ticker']['lowestAsk']) * 1.15 * amount,
            'ticker': ticker,
            'currency': currency,
            'api_url': API_URL,
            'exchange_name': 'OKX'
        }
    except Exception as e:
        print(e)
        return None


if __name__ == "__main__":
    print(fetch_price_from_okx('BTC', 1,'PLN'))
