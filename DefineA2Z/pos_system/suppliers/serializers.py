from dataclasses import fields
from pyexpat import model
from suppliers.models import *
from rest_framework import serializers


class SuppliersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suppliers
        fields = '__all__'

class SupplierOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierOrders
        fields = '__all__'


class ProductSupplierOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSupplierOrder
        fields = '__all__'

class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'