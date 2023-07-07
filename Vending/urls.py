from django.urls import path
from .views import showproduct
from .views import confirmation
from .views import delivery
from .views import refund
from .views import payment
from .views import insufficient_balance
from .views import login
from .views import register

app_name = 'Vending'
urlpatterns = [
    path('',showproduct.ShowProduct.as_view(),name = 'select'),
    path('confirmation/',confirmation.Confirmation.as_view(),name = 'confirmation'),
    path('payment/',payment.Payment.as_view(),name='payment'),
    path('insufficient/',insufficient_balance.InsufficientBalance.as_view(),name = 'insufficient_balance'),
    path('delivery/',delivery.Delivery.as_view(),name='delivery'),
    path('refund/',refund.Refund.as_view(),name='refund'),
    path('login/',login.Login.as_view(),name = 'login'),
    path('register/',register.Register.as_view(),name = 'register'),
]