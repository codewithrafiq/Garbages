from email.mime import image
from importlib.resources import path
from django.urls import path
from .views import HomePageView,locationGeoJSON,districtGeoJSON,countryGeoJSON


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('location_data/', locationGeoJSON, name='location'),
    path('district_data/', districtGeoJSON, name='district'),
    path('country_data/', countryGeoJSON, name='country'),
]
