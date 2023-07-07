from django.shortcuts import render,redirect
from Vending.models.Product import Product
from Vending.models.transaction import Transaction
from Vending.models.order import Order
from django.views import View



class Refund(View):
  def get(self,request):
    if request.session["urls"] == "refund": 
      # request.session["urls"] = None
      object_transaction=Transaction.objects.get(id=request.session["transaction_id"])
      object_order=Order.objects.filter(Transaction_id = object_transaction)
      for i in object_order:
        object_product=Product.objects.get(item_name = i.product_id)
        object_product.item_in_stock = object_product.item_in_stock + i.quantity
        object_product.save()
      object_transaction.status="Refund" 
      object_transaction.save()    
      return render (request,'refund.html',{'object_transaction':object_transaction})
    else:
      urls = request.session.get("urls")
      return redirect(f'/{urls}') 
  def post(self,request):
    request.session["urls"] = None
    return redirect("/")