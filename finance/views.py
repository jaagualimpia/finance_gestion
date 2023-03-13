from types import NoneType
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .forms import LogInForm, RegisterForm, TransactionForm
from .models import *
from django.db.models import Sum

# Create your views here.

def home(request):
    context = {}
    user = User.objects.get(username = request.session['username'])

    positive_transactions = Transaction.objects.filter(user_id = 'Jorge Agualimpia', transaction_type = True).aggregate(Sum('amount'))['amount__sum']
    negative_transactions = Transaction.objects.filter(user_id = 'Jorge Agualimpia', transaction_type = False).aggregate(Sum('amount'))['amount__sum']
    
    if positive_transactions == None:
        positive_transactions = 0    

    if negative_transactions == None:
        negative_transactions = 0

    context['balance'] = "{:,}".format(positive_transactions - negative_transactions)
    context['user'] = user.username
    
    if (positive_transactions - negative_transactions) < 0:
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
            user = User.objects.getc(username=username, password=password)

            request.session['username'] = user.username 
            request.session['password'] = user.password

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
                request.session['password'] = usuario.password 

                return redirect('/finance/home')
            
            except User.DoesNotExist as error:
                return HttpResponseRedirect('/finance/login')

    return render(request, 'finance/html/login.html') 

@csrf_exempt
def transaction(request):
    context = {}

    context['pockets'] = Pocket.objects.filter(user_id = request.session['username'])

    if request.method == 'POST':
        form = TransactionForm(request.POST)

        if form.is_valid():
            makeTransaction(form, request)
        else:
            print(request.POST)
            print(request)
            for error_field in form.errors:
                print(f"field: {error_field}")
                print(f"error: {form.errors[error_field]}" )
            

    return render(request, 'finance/html/transaction.html')

def history(request):    
    transactions = Transaction.objects.filter(user_id = "Jorge Agualimpia").order_by('-date')

    return render(request, 'finance/html/history.html', {"transactions": transactions})

def graphs(request):
    return render(request, 'finance/html/graphs.html')

def history_detail(request):
    return render(request, 'finance/html/history.html')

def pockets(request):
    return render(request, 'finance/html/pockets.html')


def makeTransaction(form, request):
    Transaction(description = form.cleaned_data.get('description'),
                amount = form.cleaned_data.get('amount'), 
                date = form.cleaned_data.get('date'), 
                user_id = User.objects.get(username = request.session['username']), 
                transaction_type = form.cleaned_data.get('transaction_type'),
                isPocketTransaction = False).save()



