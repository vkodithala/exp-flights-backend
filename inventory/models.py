from django.db import models

class Item(models.Model):
    prev = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='next_items')
    stock_id = models.PositiveIntegerField(primary_key=True)
    status = models.TextField(default="Unfulfilled")
    product_id = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    warehouse_id = models.ForeignKey('Warehouse', on_delete=models.SET_NULL, null=True)
    next = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='prev_items')

class Product(models.Model):
    product_name = models.CharField(max_length=100, primary_key=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.IntegerField()

class Warehouse(models.Model):
    warehouse_name = models.CharField(max_length=100, primary_key=True)
    location = models.CharField(max_length=100)
    capacity = models.IntegerField()

