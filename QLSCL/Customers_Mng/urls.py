from django.urls import path
from . import views

urlpatterns = [
    path('Customers/', views.Customer, name='Customers'),
]