from django.contrib import admin
from django.urls import path, re_path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.views.generic import TemplateView
from django.conf.urls.static import static


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path("api/",include('faceapp.urls')),

    # Api Documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

   re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
    ]