from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SkillViewSet

# Router do DRF que gera automaticamente as URLs
router = DefaultRouter()
router.register(r'skills', SkillViewSet, basename='skill')

urlpatterns = [
    path('', include(router.urls)),
]
