from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'finance/html/home.html') 

def register(request):
    return render(request, 'finance/html/register.html') 

def login(request):
    return render(request, 'finance/html/login.html') 

def transaction(request):
    return render(request, 'finance/transaction.html')

def history(request):
    return render(request, 'finance/history.html')

def graphs(request):
    return render(request, 'finance/graphs.html')

def history_detail(request):
    return render(request, 'finance/history.html')