from ..models import Transaction, BalanceStatistics, User
from datetime import datetime
from ..services import users_service as userv
from django.db.models import Sum

def post_transaction(form, username: str):
    date = datetime.now()
    form_date = form.cleaned_data.get('date')
    trigger = str(form_date) == f"{date.year}-{'0' if date.month < 10 else ''}{date.month}-{date.day}"

    Transaction(description = form.cleaned_data.get('description'),
                amount = form.cleaned_data.get('amount'), 
                date = form.cleaned_data.get('date'), 
                user_id = userv.get_user_by_username(username), 
                transaction_type = True if form.cleaned_data.get('transaction_type') == "ingreso" else False,
                isPocketTransaction = False).save()
    
    BalanceStatistics(user = userv.get_user_by_username(username),
                       balance = calculate_balance(username),
                       date = date if trigger else form.cleaned_data.get('date')).save()

def get_transactions_ordered_by_date(username: str):
    return Transaction.objects.filter(user_id = username).order_by('-date')

def get_balance_statistics_by_username(username: str):
    return BalanceStatistics.objects.filter(user = userv.get_user_by_username(username)).values_list('date', 'balance')


def calculate_balance(username: str) ->  float:
    positive_transactions = Transaction.objects.filter(user_id = username, transaction_type = True).aggregate(Sum('amount'))['amount__sum']
    negative_transactions = Transaction.objects.filter(user_id = username, transaction_type = False).aggregate(Sum('amount'))['amount__sum']
    
    if positive_transactions == None:
        positive_transactions = 0    

    if negative_transactions == None:
        negative_transactions = 0

    return positive_transactions - negative_transactions