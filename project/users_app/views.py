from django.shortcuts import render
from django.http import HttpResponse
from .models import Users
# Create your views here.
def renderHtml(request, username, age):
    new_user = Users(username=username, age=age)
    new_user.save()
    return render(request, "users_app/index.html", {"username": username, "age": age})

def hiID(request, id):
    return render(request, "users_app/hi.html", {"id": id})