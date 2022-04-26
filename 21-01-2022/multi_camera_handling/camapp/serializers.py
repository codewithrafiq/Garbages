from rest_framework import serializers
from .models import *



class CamaraSerializers(serializers.modelSerializer):
    class Meta:
        model = Camara
        fields = '__all__'