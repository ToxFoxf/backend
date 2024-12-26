from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def renderHtml(request, username, age):
    new_user = Users(username=username, phoneNumber=phoneNumber)
    new_user.save()
    return render(request, "users_app/index.html", {"username": username, "age": age})

def hiID(request, id):
    return render(request, "users_app/hi.html", {"id": id})