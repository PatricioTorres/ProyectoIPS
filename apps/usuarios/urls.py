from django.contrib import admin
from django.urls import path,include

from apps.usuarios.views import *

urlpatterns = [
    path('', index,name='index'),
    path('logout',logout,name='logout'),
    path('registroLineas',lineas_list,name='lineaslist')
]
