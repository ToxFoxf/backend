from . import views
from django.urls import path
urlpatterns= [
    path('robot/', views.Robots, name="robot")
]