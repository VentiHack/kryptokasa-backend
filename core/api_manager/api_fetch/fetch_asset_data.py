from core.api_manager.api_fetch.binance import fetch_price_from_binance
from core.api_manager.api_fetch.zonda import fetch_price_from_zonda


def fetch_asset_data(ticker: str, amount: float):
    zonda_data = fetch_price_from_zonda(ticker, amount, 'PLN')
    binance_data = fetch_price_from_binance(ticker, amount, 'PLN')
    data = [
        zonda_data,
        binance_data
    ]
    average_unit_price = sum(
        list(map(lambda e: e['unit_price'], data))
    ) / (len(data))
    average_asset_price = sum(
        list(map(lambda e: e['asset_price'], data))
    ) / (len(data))

    return data


if __name__ == "__main__":
    print(fetch_asset_data('BTC', 0.5))
