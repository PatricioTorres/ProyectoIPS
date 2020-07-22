from django.shortcuts import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Create your views here.

def index(request):
    return render(request, 'usuarios/index.html')

def login(request):
    return render(request, 'usuarios/login.html')
