from rest_framework.routers import SimpleRouter

from core.api_manager.views.pricing import PricingView
from core.api_manager.views.report import ReportView
from core.api_manager.viewsets.asset import AssetViewSet
from core.user.viewsets import UserViewSet
from core.auth.viewsets import LoginViewSet, RegistrationViewSet, RefreshViewSet
from django.urls import path

routes = SimpleRouter()

# AUTHENTICATION
routes.register(r'auth/login', LoginViewSet, basename='auth-login')
routes.register(r'auth/register', RegistrationViewSet, basename='auth-register')
routes.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

# ASSETS
routes.register(r'assets', AssetViewSet,
                basename='assets')

# USER
routes.register(r'user', UserViewSet, basename='user')
urlpatterns = [
    path("pricing/", PricingView.as_view(), name="pricing"),
    path("report/", ReportView.as_view(), name="report"),
    *routes.urls
]
