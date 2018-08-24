from django.urls import path
from . import views

urlPatterns = [
    path('', views.register, name = 'register'),
]