import datetime

from core.api_manager.api_fetch.binance import fetch_price_from_binance
from core.api_manager.api_fetch.zonda import fetch_price_from_zonda


def fetch_asset_data(asset):
    ticker = asset['ticker']
    amount = asset['amount']
    zonda_data = fetch_price_from_zonda(ticker, amount, 'PLN')
    binance_data = fetch_price_from_binance(ticker, amount, 'PLN')
    providers_data_list = [
        zonda_data,
        binance_data
    ]
    average_unit_price = sum(
        list(map(lambda e: e['unit_price'], providers_data_list))
    ) / (len(providers_data_list))
    average_asset_price = sum(
        list(map(lambda e: e['asset_price'], providers_data_list))
    ) / (len(providers_data_list))
    data = {
        'providers_data': providers_data_list,
        'time': datetime.datetime.now()
    }
    return data


if __name__ == "__main__":
    print(fetch_asset_data({
        'ticker': 'BTC',
        'amount': 1
    }))
