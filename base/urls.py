#!/usr/bin/env python
# encoding: utf-8

from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url

admin.autodiscover()

schema_view = get_schema_view(
   openapi.Info(
      title="Openeats API",
      default_version='v1',
    #   description="Test description",
    #   terms_of_service="https://www.google.com/policies/terms/",
    #   contact=openapi.Contact(email="contact@snippets.local"),
    #   license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Backend REST API
    path('api/v1/', include('v1.urls', namespace='v1')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # drf_yasg
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Generic Static Home
    path('', TemplateView.as_view(template_name='index.html'), name='home'),

    # Admin
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
