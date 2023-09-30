from core.api_manager.models.asset import Asset
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.response import Response

from core.api_manager.serializers.asset import AssetSerializer


class AssetViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'put', 'patch', 'post']
    serializer_class = AssetSerializer
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # if self.request.user.is_superuser:
        return Asset.objects.all().order_by('ticker')

    