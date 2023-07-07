from django.contrib import admin
from Vending.models.Product import Product
from Vending.models.transaction import Transaction
from Vending.models.order import Order
# Register your models here.
admin.site.register(Product)
admin.site.register(Transaction)
admin.site.register(Order)