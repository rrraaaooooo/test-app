from django.db import models
from .Product import Product
from .transaction import Transaction

class Order(models.Model):
  product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
  price=models.IntegerField(null=True, blank=True)
  quantity = models.IntegerField()
  Transaction_id = models.ForeignKey(Transaction , on_delete=models.CASCADE )
