from . import views
from django.urls import path

urlpatterns =[
    path("helloworld/", views.renderHtml, name="helloworld"),
    path("hi/<str:username>/<int:age>", views.renderHtml, name="hi"),
    path("hello/<int:id>", views.hiID, name="hello"),
]