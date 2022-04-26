from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from common_utils.make_fastapi_files import make_camara, run_camara
from .models import Camara
import os
from django.views import View
from django.http import HttpResponse





class HomeView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'message': 'Hello, World!'})


class CreateCamara(View):
    def get(self, request, *args, **kwargs):
        for camara in Camara.objects.all():
            make_camara(camara.name,camara.port)
        return HttpResponse("<h1>Camera Created Successfully</h1>")

class RunCamara(View):
    def get(self, request, *args, **kwargs):
        for camara in Camara.objects.all():
            run_camara(camara.name)
        return HttpResponse("<h1>Camera Started Successfully</h1>")
