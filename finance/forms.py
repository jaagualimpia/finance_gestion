from django import forms

class LogInForm(forms.Form):
    username = forms.CharField(label='username', max_length=50)
    password = forms.CharField(label='password')

class RegisterForm(forms.Form):
    username = forms.CharField(label = 'username', max_length=50)
    password = forms.CharField(label = 'password')
    rePassword = forms.CharField(label = 'rePassword')

class TransactionForm(forms.Form):
    amount =  forms.FloatField(label = 'amount')
    description =  forms.CharField(label = 'description')
    date =  forms.DateField(label = 'date')
    transaction_type =  forms.BooleanField(label = 'transaction_type')
