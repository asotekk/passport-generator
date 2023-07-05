from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, "generator/home.html")

def about(request):
    return render(request, "generator/about.html")

def password(request):

    character = list("abcdefghijklmnopqrstuyxz")
    thepassword = ""

    if request.GET.get("Uppercase"):
        character.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    if request.GET.get("Uppercase"):
        character.extend(list("#@$%&*^!?"))
    
    if request.GET.get("numbers"):
        character.extend(list("0123456789"))


    lenght = int(request.GET.get("lenght"))

    for x in range(lenght):
        thepassword += random.choice(character)

    return render(request, "generator/password.html", {"password": thepassword})