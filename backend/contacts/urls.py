from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet

# Router do DRF que gera automaticamente as URLs
router = DefaultRouter()
router.register(r'', ContactViewSet, basename='contact')

urlpatterns = [
    path('', include(router.urls)),
]
