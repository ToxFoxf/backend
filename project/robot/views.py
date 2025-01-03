from django.shortcuts import render
from .models import Robots
def data(request, name, color):
    new_robot = Robots(name=name, color=color)
    new_robot.save()
    return(request, "robots_app/index.html", {"name": name, "color": color})