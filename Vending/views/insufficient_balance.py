from django.shortcuts import render,redirect
# from Vending.models.Product import Product
from Vending.models.transaction import Transaction
from django.views import View

class InsufficientBalance(View):
  
  def get(self,request):
    if request.session["urls"] == "insufficient":
      object_transaction = Transaction.objects.get(id = request.session["transaction_id"])
      return render(request,'insufficient_balance.html',{'object_transaction':object_transaction})
    else:
      urls = request.session.get("urls")
      return redirect(f'/{urls}') 
  def post(self,request):
    form_object=request.POST
    if form_object["choice"] == "insert":
      request.session["urls"]="payment"
      return redirect('/payment')
    else:
      request.session["urls"] = "refund"
      return redirect('/refund')  