from rest_framework import serializers
from .models import *





class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class UnitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unites
        fields = '__all__'

class CurrenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currencies
        fields = '__all__'

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'
        # depth = 1

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductStocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductStocks
        fields = '__all__'

class DiscountVariationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountVariations
        fields = '__all__'

class PriceVariationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceVariations
        fields = '__all__'

class ProductColorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColors
        fields = '__all__'


# class ShippingAddressSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ShippingAddress
#         fields = '__all__'

# class OrdersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Orders
#         fields = '__all__'

# class CustomersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customers
#         fields = '__all__'

# class ProductOrdersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductOrders
#         fields = '__all__'