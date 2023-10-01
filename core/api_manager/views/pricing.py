import json

from django.forms import model_to_dict
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from core.api_manager.api_fetch.fetch_asset_data import fetch_asset_data
from core.api_manager.models.report import Report


@method_decorator(csrf_exempt, name='dispatch')
class PricingView(View):
    def post(self, request, *args, **kwargs):
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        pricing_results = []
        for asset in body_data['assets']:
            asset_data = fetch_asset_data(asset)
            pricing_results.append(asset_data)
        report_data = {
            'nazwa_organu_egzekucyjnego': body_data['nazwa_organu_egzekucyjnego'],
            'nr_sprawy': body_data['nr_sprawy'],
            'owner_data': body_data['owner_data']
        }
        report = Report.objects.create(**report_data)
        return JsonResponse({
            'pricing_results': pricing_results,
            'report': model_to_dict(report)
        }, safe=False)
