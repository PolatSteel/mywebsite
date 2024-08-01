from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base/home.html')        

def information(request):
    return render(request, 'base/information.html')

def start(request):
    return render(request, 'base/start.html')

def contact(request):
    return render(request, 'base/contact.html')