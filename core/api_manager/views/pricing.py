import json

from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from core.api_manager.api_fetch.fetch_asset_data import fetch_asset_data


@method_decorator(csrf_exempt, name='dispatch')
class PricingView(View):
    def post(self, request, *args, **kwargs):
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        for asset in body_data['assets']:
            asset_data = fetch_asset_data(asset)
            print(asset_data)

        return JsonResponse({"msg":"ok"})
