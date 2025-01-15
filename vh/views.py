from django.shortcuts import render
from django.http import HttpResponse
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zayn.settings')
django.setup()

from .models import Users

# Your code here

def index(request):





    return render(request,'index.html')

# Create your views here.
def v1(response):
    return HttpResponse("<h1>welcome<h1/>")


def add(request):
    name = request.POST.get('name')
    size = request.POST.get('size')
    address = request.POST.get('address')

    User = Users(name=name, size=size, address=address)
    User.save()

    naam=request.POST['name'].upper()
    return render(request,"result.html",    {'user':naam})