from django.db import models
from common_utils.BaseClass import BaseModel



class Suppliers(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SupplierOrders(BaseModel):
    supplier_id = models.ForeignKey(Suppliers, on_delete=models.CASCADE)
    branch_id = models.IntegerField(default=0)
    total_quantity = models.FloatField(default=0)
    discount = models.FloatField(default=0)
    vat = models.FloatField(default=0)
    sub_total = models.FloatField(default=0)
    grand_amount = models.FloatField(default=0)

class ProductSupplierOrder(BaseModel):
    product_id = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    supplier_order_id = models.ForeignKey(SupplierOrders, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)
    return_quantity = models.FloatField(default=0)
    barcodes = models.JSONField()
    return_barcodes = models.JSONField()
    unit_id = models.ForeignKey('products.Unites', on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    status = models.CharField(max_length=100)


class Payments(BaseModel):
    supplier_id = models.ForeignKey(Suppliers, on_delete=models.CASCADE)
    supplier_order_id = models.ForeignKey(SupplierOrders, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    unique_id = models.CharField(max_length=100)
    payment_type = models.CharField(max_length=100)
    payment_date = models.DateTimeField()
    payment_methods = models.CharField(max_length=100)
    payment_details = models.CharField(max_length=100)