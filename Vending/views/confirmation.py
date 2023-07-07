from django.shortcuts import render,redirect
from Vending.models.Product import Product
from Vending.models.order import Order
from Vending.models.transaction import Transaction

from django.views import View

class Confirmation(View):
  def get(self,request):
    if request.session["urls"]=="confirmation":  
      object_transaction = Transaction.objects.get(id = request.session["transaction_id"])
      object_order = Order.objects.filter(Transaction_id = object_transaction)
      return render(request,'confirmation.html',{"object_transaction":object_transaction,
                                                 "object_order":object_order,
                                                 })
    else:
      urls = request.session.get("urls")
      return redirect(f'/{urls}')   
  def post(self,request):
    if request.POST["choice"] == "yes":
      object_transaction = Transaction.objects.get(id = request.session["transaction_id"])
      object_transaction.status="Confirm"
      object_transaction.save()
      request.session["urls"] = "delivery"
      return redirect('/delivery')
    else:
        request.session["urls"] = "refund"
        return redirect("/refund")
        
    
    