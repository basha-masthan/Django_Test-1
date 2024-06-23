from django.urls import path
from .views import *

urlpatterns = [
    path('',home),
    path('register/',register),
    path('login/',login),
    path('usrp/',login_required(usrp)),
    path('usrpage/',usrpage),
    path('logout/',logout),
    path('usredit/',usredit),
]