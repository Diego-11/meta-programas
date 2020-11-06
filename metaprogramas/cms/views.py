from django.shortcuts import render
from .models import WelcomeScreen

# Create your views here.


def welcome(request):

    screen = WelcomeScreen.objects.last()
    return render(request, 'cms/welcome.html', {'screen': screen,
                                                'title': 'Bienvenida'})


def login(request):

    return render(request, 'cms/login.html')
