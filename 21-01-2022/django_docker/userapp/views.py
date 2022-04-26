from rest_framework.response import Response
from django.contrib.auth.models import User, Group, Permission
from rest_framework.views import APIView
# Decorators
from common_utiles.decorator import if_log_then_go, my_permission_chk
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth import authenticate, login, logout
from django.core.serializers import serialize


class TestClass(APIView):
    def get(self, request, format=None):
        print("Users:", User.objects.all())
        print("Groups:", Group.objects.all())
        print("Permissions:", Permission.objects.all())
        user = User.objects.get()
        return Response({"message": "Hello, world!"})