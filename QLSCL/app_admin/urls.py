from django.urls import path
from . import views

urlpatterns = [
    path('Courts/', views.Court, name='Courts'),
    path('Customers/', views.Customer, name='Customers'),
]