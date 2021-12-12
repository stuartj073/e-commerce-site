from django.urls import path
from . import views

""" Paths to each page from the home app """

urlpatterns = [
    path('', views.checkout, name='checkout')
]
