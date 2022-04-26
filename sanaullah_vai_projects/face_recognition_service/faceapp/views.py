from traceback import print_tb
from matplotlib import image
from matplotlib.pyplot import cla
from rest_framework import permissions
from rest_framework import authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.faceauth import registration_new_face,recognition_face




class Registration(APIView):
    def post(self,request):
        # print("Registration",request.data)
        response = registration_new_face(request.data['file'],request.data['name'])
        return Response(response)

class Login(APIView):
    def post(self,request):
        # print("Login",request.data)
        response = recognition_face(request.data['file'])
        return Response(response)