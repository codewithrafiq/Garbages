from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from .models import *



class HomePageView(TemplateView):
    template_name = 'index.html'


def locationGeoJSON(request):
    data = serialize('geojson', Location.objects.all())
    return HttpResponse(data, content_type='json')

def districtGeoJSON(request):
    data = serialize('geojson', District.objects.all()[:30])
    return HttpResponse(data, content_type='json')

def countryGeoJSON(request):
    data = serialize('geojson', Country.objects.all())
    return HttpResponse(data, content_type='json')