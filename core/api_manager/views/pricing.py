import json

from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class PricingView(View):
    def post(self, request, *args, **kwargs):
        body_unicode = request.body.decode('utf-8')
        print(request)
        body_data = json.loads(body_unicode)
        print(body_data)
        data = get_pricing()
        return JsonResponse()
