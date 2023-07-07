from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate



class Login(View):
  def get(self,request):
    return render(request,'login.html')
  def post(self,request):
    form_object=request.POST
    if User.objects.filter(username=form_object["username"]).exists():
      user=authenticate(username = form_object["username"], password = form_object["password"])
      if user is None:
        messages.info(request,'Incorrect Password')
        return redirect("/login/")
      else:
        return redirect("/")
        
        
    