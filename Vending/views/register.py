from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages

class Register(View):
  def get(self,request):
    return render(request,'register.html')
  def post(self,request):
    form_object=request.POST
    user =User.objects.filter(username = form_object["username"])
    if user.exists():
      messages.info(request,'Username already taken')
      return redirect("/register/")
    user = User(username = form_object["username"])
    user.set_password(form_object["password"])
    user.save()
    return redirect("/login")