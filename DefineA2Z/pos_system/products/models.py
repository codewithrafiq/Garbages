from re import sub
from django.forms import BaseModelFormSet
from common_utils.BaseClass import BaseModel
from django.db import models
import uuid



class Color(BaseModel):
    name = models.CharField(max_length=255)
    position = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Brand(BaseModel):
    name = models.CharField(max_length=200)
    logo = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Unites(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Currencies(BaseModel):
    name = models.CharField(max_length=200)
    symbol = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Categorie(BaseModel):
    name = models.CharField(max_length=200)
    deescription = models.TextField(null=True, blank=True)
    logo = models.TextField(null=True, blank=True)
    # sub_categorie = models.ManyToManyField('self', blank=True)
    # root_categorie = models.ForeignKey('self', blank=True,null=True, related_name='root_categories', on_delete=models.CASCADE)
    sub_categorie = models.ForeignKey('self',related_name='sub_categories', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Product(BaseModel):
    name = models.CharField(max_length=200)
    branch_id = models.IntegerField(default=0)
    category_id = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    sub_category_id = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='sub_category_id')
    sub_sub_category_id = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='sub_sub_category_id')
    property_option = models.JSONField(null=True, blank=True)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    unit_id = models.ForeignKey(Unites, on_delete=models.CASCADE)
    currency_id = models.ForeignKey(Currencies, on_delete=models.CASCADE)
    weight = models.FloatField(default=0)
    length = models.FloatField(default=0)
    width = models.FloatField(default=0)
    height = models.FloatField(default=0)
    tags = models.JSONField(null=True, blank=True)
    product_type = models.CharField(max_length=200)
    photos = models.JSONField(null=True, blank=True)
    thumnail_img = models.TextField(null=True, blank=True)
    color_type = models.FloatField(max_length=200)
    colors = models.JSONField(null=True, blank=True)
    color_images = models.JSONField(null=True, blank=True)
    attributes = models.JSONField(null=True, blank=True)
    attribute_options = models.JSONField(null=True, blank=True)
    discount = models.FloatField(default=0)
    discount_type = models.CharField(max_length=200)
    discount_variation = models.FloatField(default=0)
    tax = models.FloatField(default=0)
    tax_type = models.FloatField(max_length=200)
    orderQtyLimit = models.BooleanField(default=False)
    orderQtyLimitMin = models.IntegerField(default=0)
    orderQtyLimitMax = models.IntegerField(default=0)
    unit_price = models.FloatField(default=0)
    price_variation = models.FloatField(default=0)
    stockManagement = models.BooleanField(default=False)
    quantity = models.IntegerField(default=0)
    sku = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    slug = models.TextField(null=True, blank=True)

class ProductStocks(BaseModel):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    variant = models.JSONField()
    sku = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    quantity = models.FloatField(null=True, blank=True)

class DiscountVariations(BaseModel):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='discount_variations')
    percent_off = models.FloatField(default=0)
    minQty = models.IntegerField(default=0)

class PriceVariations(BaseModel):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='price_variations')
    off_price = models.FloatField(default=0)
    minQty = models.FloatField(default=0)
    maxQty = models.FloatField(default=0)

class ProductColors(BaseModel):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    color_id = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='color_id')




# ---------------------------------------------------------------------------


# class ShippingAddress(BaseModel):
#     customer_id = models.ForeignKey('products.Customer', on_delete=models.CASCADE)
#     division_id = models.IntegerField()
#     district_id = models.IntegerField()
#     thana_upozila_id = models.IntegerField()
#     address = models.TextField()

# class Orders(BaseModel):
#     branch_id = models.ForeignKey('employee.Branches', on_delete=models.CASCADE)
#     customer_id = models.ForeignKey("products.Customers", on_delete=models.CASCADE)
#     shippping_address_id = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE)
#     products = models.ForeignKey(Product, on_delete=models.CASCADE)
#     total_qty = models.IntegerField(default=0)
#     sub_total = models.FloatField(default=0)
#     tax = models.FloatField(default=0)
#     discount = models.FloatField(default=0)
#     total = models.FloatField(default=0)

# class Customers(BaseModel):
#     name = models.CharField(max_length=200)

# class ProductOrders(BaseModel):
#     product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
#     order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
#     unit_price = models.FloatField(default=0)
#     quantity = models.IntegerField(default=0)
#     amount = models.FloatField(default=0)
#     status = models.IntegerField(max_length=200)
#     return_qty = models.IntegerField(default=0)
#     return_price = models.FloatField(default=0)
#     skues = models.JSONField()
#     return_skues = models.JSONField()

