from rest_framework.serializers import ModelSerializer
from testapp.models import  *


class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'