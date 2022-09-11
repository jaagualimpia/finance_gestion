from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('trasaction', views.transaction, name='transaction'),
    path('history', views.history, name='history'),
    path('history_detail', views.history_detail, name='history'),
    path('graphs', views.graphs, name='graphs')
]