from django.urls import path
from .views import CreateCamara,RunCamara

urlpatterns = [
    path('camaras/', CreateCamara.as_view()),
    path('camaras_run/', RunCamara.as_view()),
]
