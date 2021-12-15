from django.urls import path
from . import views
from .webhooks import webhook

""" Paths to each page from the home app """

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('wh', webhook, name='webhook')
]
