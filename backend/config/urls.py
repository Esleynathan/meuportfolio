"""
URL configuration for config project.
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.static import serve
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    # A URL do admin foi alterada de 'admin/' para 'x/' por segurança.
    path('x/', admin.site.urls),

    # API Endpoints
    path('api/', include('projects.urls')),
    path('api/', include('skills.urls')),
    path('api/', include('contacts.urls')),

    # API Documentation (Swagger)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]

# Serve media files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    # Em produção, serve media files via Django (WhiteNoise não serve media por padrão)
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]

# SPA Fallback - Serve o Angular para qualquer rota não encontrada
# Deve ser a última rota para não interferir com /api, /x, /static, /media
if settings.FRONTEND_DIR.exists():
    urlpatterns += [
        re_path(r'^(?!api/|x/|static/|media/).*$', TemplateView.as_view(template_name='index.html')),
    ]
