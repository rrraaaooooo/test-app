from django.shortcuts import render,redirect
from Vending.models.Product import Product
from Vending.models.order import Order
from Vending.models.transaction import Transaction
from django.views import View


class Delivery(View):
  def get(self,request):
    if request.session["urls"]=="delivery":
      object_transaction=Transaction.objects.get(id=request.session['transaction_id'])
      object_transaction.status="Delivered"
      object_transaction.save()
      object_order=Order.objects.filter(Transaction_id =object_transaction)
      list_=list(Transaction.objects.filter(status = "Delivered"))
      print(list_)
      # object_product=Product.objects.all()
      return_amount = object_transaction.amount - object_transaction.cost_of_product 
      return render (request,'bill.html',{'return_amount':return_amount,
                                          'object_transaction':object_transaction,
                                          'object_order':object_order
                                          })
    
    else: 
      urls = request.session.get("urls")
      return redirect(f'/{urls}') 
  def post(self,request):
    request.session["urls"] = None
    return redirect("/")     