import pandas as pd
import numpy as np
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .forms import LogInForm, RegisterForm, TransactionForm
from .models import *
from django.db.models import Sum
from datetime import datetime
from sklearn.linear_model import LinearRegression

# Create your views here.

def home(request):
    context = {}
    user = User.objects.get(username = request.session['username'])

    balance = calculate_balance(request)
    context['balance'] = "{:,}".format(balance)
    context['user'] = user.username
    
    if (balance) < 0:
        context['positive'] = False
    else:
        context['positive'] = True

    return render(request, 'finance/html/home.html', context=context) 

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            User(username=username, password=password).save()
            user = User.objects.get(username=username, password=password)

            request.session['username'] = user.username 

            return redirect('/finance/home')

    return render(request, 'finance/html/register.html') 

def login(request):
    if request.method == 'GET':
        form = LogInForm(request.GET)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            try:
                usuario = User.objects.get(username = username, password = password)
                request.session['username'] = usuario.username

                return redirect('/finance/home')
            
            except User.DoesNotExist as error:
                return HttpResponseRedirect('/finance/login')

    return render(request, 'finance/html/login.html') 

@csrf_exempt
def transaction(request):

    if request.method == 'POST':
        form = TransactionForm(request.POST)

        if form.is_valid():
            make_transaction(form, request)
        else:
            print_errors(form, request)
            
    return render(request, 'finance/html/transaction.html')

def history(request):    
    transactions = Transaction.objects.filter(user_id = request.session['username']).order_by('-date')

    return render(request, 'finance/html/history.html', {"transactions": transactions})

def graphs(request):
    context = { "date": [], "balance": []}

    data_dict = BalanceStatistics.objects.filter(user = User(username = request.session['username'])).values_list('date', 'balance')

    for element in data_dict:
        context['date'].append( element[0])
        context['balance'].append(element[1])

    df_context = pd.DataFrame(context)
    df_context['date'].apply(func = pd.to_datetime)
    df_context['date'] = df_context['date'].apply(oordinal_modified_transform)

    model = LinearRegression().fit(X = np.array(df_context['date']).reshape(-1, 1), y = df_context['balance'])
    ordinal_date = datetime.toordinal(datetime.strptime('2023/04/20', "%Y/%m/%d"))
    prediction = model.predict([[ordinal_date]])
    print(prediction[0])
    return render(request, 'finance/html/graphs.html', context = context)

def history_detail(request):
    return render(request, 'finance/html/history.html')

def pockets(request):
    return render(request, 'finance/html/pockets.html')


def make_transaction(form, request):
    date = datetime.now()
    form_date = form.cleaned_data.get('date')
    trigger = str(form_date) == f"{date.year}-{'0' if date.month < 10 else ''}{date.month}-{date.day}"

    Transaction(description = form.cleaned_data.get('description'),
                amount = form.cleaned_data.get('amount'), 
                date = form.cleaned_data.get('date'), 
                user_id = User.objects.get(username = request.session['username']), 
                transaction_type = True if form.cleaned_data.get('transaction_type') == "ingreso" else False,
                isPocketTransaction = False).save()
    
    BalanceStatistics(user = User.objects.get(username = request.session['username']),
                       balance = calculate_balance(request),
                       date = date if trigger else form.cleaned_data.get('date')).save()

def print_errors(form, request):
    print(request.POST)
    for error_field in form.errors:
                    print(f"field: {error_field}")
                    print(f"error: {form.errors[error_field]}" )

def calculate_balance(request):
    positive_transactions = Transaction.objects.filter(user_id = request.session['username'], transaction_type = True).aggregate(Sum('amount'))['amount__sum']
    negative_transactions = Transaction.objects.filter(user_id = request.session['username'], transaction_type = False).aggregate(Sum('amount'))['amount__sum']
    
    if positive_transactions == None:
        positive_transactions = 0    

    if negative_transactions == None:
        negative_transactions = 0

    return positive_transactions - negative_transactions

def oordinal_modified_transform(date: datetime):
    return datetime.toordinal(date) + (date.hour/24)+ (date.minute/1440) + (date.second/86400)