from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import LogInForm, RegisterForm
from .models import *

# Create your views here.

def home(request):
    return render(request, 'finance/html/home.html') 

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            User(username=username, password=password).save()

            return redirect('/finance/home')

    return render(request, 'finance/html/register.html') 

def login(request):
    if request.method == 'GET':
        form = LogInForm(request.GET)

        if form.is_valid():
            return redirect('/finance/home')


    return render(request, 'finance/html/login.html') 

def transaction(request):
    return render(request, 'finance/transaction.html')

def history(request):
    return render(request, 'finance/history.html')

def graphs(request):
    return render(request, 'finance/graphs.html')

def history_detail(request):
    return render(request, 'finance/history.html')