import datetime

from django.forms import model_to_dict

from core.api_manager.api_fetch.binance import fetch_price_from_binance
from core.api_manager.api_fetch.okx import fetch_price_from_okx
from core.api_manager.api_fetch.zonda import fetch_price_from_zonda
from core.api_manager.models.asset import Asset


def fetch_asset_data(asset):
    assets_dict = dict()
    assets_queryset = Asset.objects.all()
    for asset_obj in assets_queryset:
        assets_dict[asset_obj.ticker] = model_to_dict(asset_obj)
    ticker = asset['ticker']
    amount = asset['amount']
    zonda_data = fetch_price_from_zonda(ticker, amount, 'PLN')
    binance_data = fetch_price_from_binance(ticker, amount, 'PLN')
    okx_data = fetch_price_from_okx(ticker, amount, 'PLN')
    providers_data_list = [
        zonda_data,
        binance_data,
        okx_data
    ]
    average_unit_price = sum(
        list(map(lambda e: e['unit_price'], providers_data_list))
    ) / (len(providers_data_list))
    average_asset_price = sum(
        list(map(lambda e: e['asset_price'], providers_data_list))
    ) / (len(providers_data_list))
    data = {
        'asset': {
            'ticker': ticker,
            'amount': amount,
            'img_url': assets_dict[ticker]['img_url'],
            'name': assets_dict[ticker]['name'],
        },
        'providers_data': providers_data_list,
        'time': datetime.datetime.now(),
        'average_unit_price': average_unit_price,
        'average_asset_price': average_asset_price,
    }
    return data


if __name__ == "__main__":
    print(fetch_asset_data({
        'ticker': 'BTC',
        'amount': 1
    }))
