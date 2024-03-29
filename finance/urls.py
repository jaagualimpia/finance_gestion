from django.urls import path
from . import views

app_name = 'finance'

urlpatterns = [
    path('home', views.home, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('transaction', views.transaction, name='transaction'),
    path('history', views.history, name='history'),
    path('history_detail', views.history_detail, name='history'),
    path('graphs', views.graphs, name='graphs'),
    path('pockets', views.pockets, name='pockets')
]