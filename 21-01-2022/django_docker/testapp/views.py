from ast import Delete
from traceback import print_tb
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, serializers
from rest_framework import authentication
from common_utiles.decorator import my_database
from django.apps import apps
from .serializers import *
from .models import *
import os
from rest_framework.authtoken.models import Token
from enumfields import EnumField


def index(request):
    return HttpResponse("<h1>Hello World</h1>")


class GetAppModels(APIView):
    # permission_classes = [permissions.IsAuthenticated,]
    # authentication_classes = [authentication.SessionAuthentication,authentication.TokenAuthentication,authentication.BasicAuthentication,]
    def get(self, request, appname, *args, **kwargs):
        """ Give me any app name I will Give you all models name """
        return Response(str([d.__name__ for d in dict(apps.all_models[appname]).values()]))


class GetModelFields(APIView):
    # permission_classes = [permissions.IsAuthenticated,]
    # authentication_classes = [authentication.SessionAuthentication,authentication.TokenAuthentication,authentication.BasicAuthentication,]
    def get(self, request, appname, modelname, *args, **kwargs):
        """ 
        Give me any app and model name I will Give you all fields Details 
        """
        result = []
        modeltype = apps.get_model(app_label=appname, model_name=modelname)
        print(modeltype._meta)
        fields = modeltype._meta.fields
        try:
            for field in fields:
                res = {}
                res["field_name"] = str(field).split('.')[2]
                res["datatype"] = str(field.__class__).split(
                    '.')[-1].replace('\'>', '')
                res["is_null"] = field.null
                if field.__class__ is EnumField:
                    res["choices"] = ["{}:{}".format(choice[1], str(
                        choice[-1])) for choice in field.choices]
                result.append(res)
            return Response(result)
        except Exception as e:
            return Response(str(e))


class AllInOne(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    authentication_classes = [authentication.TokenAuthentication,
                              authentication.SessionAuthentication,
                              authentication.BasicAuthentication, ]

    def get(self, request, appname, modelname, pk=None, *args, **kwargs):
        modeltype = apps.get_model(app_label=appname, model_name=modelname)
        modelName = str(str(modeltype._meta).split('.')[1]).capitalize()
        serializerName = modelName + 'Serializer'
        serializer = eval(serializerName)
        if pk:
            todo_objs = modeltype.objects.filter(pk=pk).first()
            serializer_instance = serializer(todo_objs)
            return Response(serializer_instance.data)
        todo_objs = modeltype.objects.all()
        print("todo_objs--------->",todo_objs)
        serializer_instance = serializer(todo_objs, many=True)
        return Response(serializer_instance.data)

    def post(self, request, appname, modelname, pk=None, *args, **kwargs):
        modeltype = apps.get_model(app_label=appname, model_name=modelname)
        modelName = str(str(modeltype._meta).split('.')[1]).capitalize()
        serializerName = modelName + 'Serializer'
        serializer = eval(serializerName)
        if pk:
            todo_objs = modeltype.objects.filter(pk=pk).first()
            serializer_instance = serializer(todo_objs, data=request.data)
            if serializer_instance.is_valid():
                serializer_instance.save()
                return Response(serializer_instance.data)
            else:
                return Response(serializer_instance.errors)
        else:
            serializer_instance = serializer(data=request.data)
            if serializer_instance.is_valid():
                serializer_instance.save()
                return Response(serializer_instance.data)
            else:
                return Response(serializer_instance.errors)

    def delete(self, request, appname, modelname, pk=None, *args, **kwargs):
        if pk:
            modeltype = apps.get_model(app_label=appname, model_name=modelname)
            todo_objs = modeltype.objects.filter(pk=pk).first()
            todo_objs.delete()
            return Response("Deleted")
        else:
            return Response("Please provide pk")


class TodoView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    authentication_classes = [authentication.TokenAuthentication,
                              authentication.SessionAuthentication, authentication.BasicAuthentication, ]

    @my_database
    def get(self, request, db, user, *args, **kwargs):
        print("db------->", db)
        print("user------->", user)
        serializer = TodoSerializer(
            Todo.objects.using(db).all(), many=True).data
        return Response(serializer)

    @my_database
    def post(self, request, db, user, *args, **kwargs):
        print("db------->", db)
        print("user------->", user)
        print("request.data------->", request.data)
        data = request.data
        data['user'] = user.id
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            Todo.objects.using(db).create(**serializer.data)
            return Response(serializer.data)
        return Response("serializer.data")


class CreateUser(APIView):
    def post(self, request, *args, **kwargs):
        try:
            print("request.data------->", request.data)
            serializer = UserSerializer(data=request.data)
            serializer.save() if serializer.is_valid() else Response("serializer.data")
            user = User.objects.get(username=request.data['username'])
            token = Token.objects.create(user=user)
            try:
                try:
                    os.makedirs('users_databases')
                except Exception as e:
                    pass
                f = open(
                    f'./users_databases/{serializer.data["username"]}.db', 'w')
                f.close()
                os.system('python3 manage.py migrate_all_db')
            except Exception as e:
                return Response({"Error": str(e)})
            return Response({"message": f"User Created as {serializer.data['username']}", "token": token.key})
        except Exception as e:
            return Response({"Error": str(e)})
