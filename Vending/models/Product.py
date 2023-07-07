from django.db import models

# Create your models here.
class Product(models.Model):
  item_name = models.CharField(max_length=30)
  item_price = models.IntegerField()
  item_in_stock = models.IntegerField()
  def __str__(self):
    return self.item_name