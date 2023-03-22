from ..models import User
from django.http import HttpResponseNotFound

def get_all_users():
    query = User.objects.all()
    return query

def get_user_by_credentials(username: str, password: str) -> User:
    try:
        return User.objects.get(username = username, password = password)
    except BaseException as error:
        return None
    
def get_user_by_username(username: str):
    return User.objects.get(username = username)

def post_user(username: str, password: str) -> User:
    try:
        User(username=username, password=password).save()
        return User.objects.get(username=username, password=password)
    
    except BaseException as error:
        return None
