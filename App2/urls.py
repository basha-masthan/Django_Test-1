from django.urls import path
from .views import *

urlpatterns = [
    path('',home),
    path('register/',register),
    path('usrpage/',usrpage),
    path('login/',login),
    path('usrp/',usrp),
    path('logout/',logout_1),
    path('cart/',usr_cart),
    path('payment/',payment),
    path('cartadd/',usrcart_add),
    path('mb/',adminpage),
    path('delcard/',delcard),
]