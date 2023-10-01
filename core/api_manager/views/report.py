import json

from django.core.files.base import ContentFile, File
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.response import Response

from core.api_manager.helpers.generate_pdf import generate_pdf


@method_decorator(csrf_exempt, name='dispatch')
class ReportView(View):
    def post(self, request, *args, **kwargs):
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        pricing_results = body_data['pricing_results']
        pdf_file_path, pdf_filename = generate_pdf(body_data)
        pdf_file = open(pdf_file_path, 'rb')
        pdf_content = ContentFile(pdf_file.read())
        pdf_file.close()
        # serializer.validated_data['pdf'] = File(pdf_content, name=pdf_file_path)
        # serializer.validated_data['pdf_url'] = pdf_url
        # self.perform_create(serializer)
        response = JsonResponse({
            # 'pdf': File(pdf_content, name=pdf_file_path),
            'pdf_file_path': pdf_file_path,
            'pdf_filename': pdf_filename,
        }, status=status.HTTP_201_CREATED)
        return response
