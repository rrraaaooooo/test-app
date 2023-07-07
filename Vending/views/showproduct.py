from django.shortcuts import render,redirect
from Vending.models.Product import Product
from Vending.models.transaction import Transaction
from Vending.models.order import Order

from django.views import View

# Create your views here.
class ShowProduct(View):
  
  def get(self,request):
    
    if request.session.get("urls")== None:
      products = Product.objects.all()
      return render(request,'showproduct.html',{'products':products})
    
    else: 
      urls = request.session.get("urls")
      return redirect(f'/{urls}')
  
  def post(self,request):
    
    form_object= request.POST                         
    object_transaction=Transaction( status="selected", amount = 0 )
    object_transaction.save()
    request.session['transaction_id'] = object_transaction.id
    
    object_product=Product.objects.all()
    cost_of_products = 0
    
    for i in object_product:
      
      if int(form_object[f'{i.item_name}']) > 0:
        
        #Calculate cost of all selected products
        cost_of_products += (i.item_price * int(form_object[f'{i.item_name}']))
        
        # manage stock 
        i.item_in_stock = i.item_in_stock - int(form_object[f'{i.item_name}'])
        i.save() 
        #create and save records of order table
        object_order=Order(product_id = i,
                           quantity = int(form_object[f'{i.item_name}']), 
                           Transaction_id = object_transaction,
                           price=i.item_price * int(form_object[f'{i.item_name}']))
        object_order.save()
    
    object_transaction=Transaction.objects.get(id = request.session['transaction_id'])
    object_transaction.cost_of_product=cost_of_products
    object_transaction.save()
    request.session["urls"] = "payment"
    return redirect('/payment')