from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .forms import LogInForm, RegisterForm, TransactionForm, PredictionForm
from datetime import datetime
from .services import users_service, transaction_service
from .services.prediction_models.balance_prediction_models import LinearRegressionBalanceStatistics

# Create your views here.

def home(request):
    context = {}
    user = users_service.get_user_by_username(username = request.session['username'])
    balance = transaction_service.calculate_balance(user.username)

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
            user = users_service.post_user(username = form.cleaned_data.get('username'), 
                                           password = form.cleaned_data.get('password'))

            request.session['username'] = user.username 

            return redirect('/finance/home')

    return render(request, 'finance/html/register.html') 

def login(request):
    if request.method == 'GET':
        form = LogInForm(request.GET)

        if form.is_valid():
            try:
                usuario = users_service.get_user_by_credentials(username = form.cleaned_data.get('username'),
                                                                password = form.cleaned_data.get('password') )
                request.session['username'] = usuario.username

                return redirect('/finance/home')
            
            except BaseException as error:
                return HttpResponseRedirect('/finance/login')

    return render(request, 'finance/html/login.html') 

@csrf_exempt
def transaction(request):

    if request.method == 'POST':
        form = TransactionForm(request.POST)

        if form.is_valid():
            transaction_service.post_transaction(form, request.session['username'])
        else:
            print_errors(form, request)
            
    return render(request, 'finance/html/transaction.html')

def history(request):    
    transactions = transaction_service.get_transactions_ordered_by_date(request.session['username'])

    return render(request, 'finance/html/history.html', {"transactions": transactions})

@csrf_exempt
def graphs(request):
    context = { "date": [], "balance": []}

    data_dict = transaction_service.get_balance_statistics_by_username(request.session['username'])

    for element in data_dict:
        context['date'].append( element[0])
        context['balance'].append(element[1])

    balance_predictor = LinearRegressionBalanceStatistics(context)

    if request.method == 'POST':
        form = PredictionForm(request.POST)

        if form.is_valid():
            prediction_date = balance_predictor.get_prediction_by_date(form.cleaned_data.get('date'))
            context['prediction'] = "{:,}".format(round(prediction_date, 2))

    return render(request, 'finance/html/graphs.html', context = context)

def history_detail(request):
    return render(request, 'finance/html/history.html')

def pockets(request):
    return render(request, 'finance/html/pockets.html')

def print_errors(form, request):
    print(request.POST)
    for error_field in form.errors:
                    print(f"field: {error_field}")
                    print(f"error: {form.errors[error_field]}" )
