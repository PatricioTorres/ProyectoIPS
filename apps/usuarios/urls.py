from django.urls import *
from apps.usuarios.views import *
urlpatterns = [
    path('', index),
    path('login', login),
]
