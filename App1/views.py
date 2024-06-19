from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1>Suku </h1>")


def wpage(request):
    return render(request,'home.html')