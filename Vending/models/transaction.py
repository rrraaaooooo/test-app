from django.db import models
from django.contrib.auth.models import User
class Transaction(models.Model):
  cost_of_product = models.IntegerField(null=True, blank=True)
  amount = models.IntegerField(null=True, blank=True)
  status = models.CharField(max_length=30 ,null=True, blank=True)
  users = models.ForeignKey(User , on_delete= models.SET_NULL ,null= True , blank=True) 
    
       