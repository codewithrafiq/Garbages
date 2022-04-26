from django.urls import path
from .views import *




urlpatterns = [
    path('', TestClass.as_view()),
]
