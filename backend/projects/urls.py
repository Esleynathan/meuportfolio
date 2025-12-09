from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet

# Router do DRF que gera automaticamente as URLs
router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')

urlpatterns = [
    path('', include(router.urls)),
]
