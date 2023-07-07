from django.shortcuts import render,redirect
# from Vending.models.Product import Product
from Vending.models.transaction import Transaction
from django.views import View


class Payment(View):
  def get(self,request):
    if request.session.get("urls") =="payment":
      return render(request,'payment.html')
    else:
      urls = request.session.get("urls")
      return redirect(f'/{urls}')  

  def post(self,request):
    object_transaction = Transaction.objects.get(id = request.session["transaction_id"])
    form_object = request.POST
    amount = object_transaction.amount + (1 * int(form_object['1coin'])
                                          + (5 * int(form_object['5coin'])) 
                                          + (10 * int(form_object['10coin']))
                                          + (25 * int(form_object['25coin']))
                                          )
    object_transaction.amount=amount
    object_transaction.status="Paid" 
    object_transaction.save()
    if object_transaction.amount >= object_transaction.cost_of_product:
      request.session["urls"] ="confirmation"
      return redirect ('/confirmation')
    else:
      request.session["urls"] = "insufficient"
      return redirect('/insufficient')
  
# def productPrice(request):
#   object=Transaction.objects.get(id= request.session['Transaction_id'])
#   print(Product.objects.get(item_name=object.product_id).item_price)
#   return Product.objects.get(item_name=object.product_id).item_price
  