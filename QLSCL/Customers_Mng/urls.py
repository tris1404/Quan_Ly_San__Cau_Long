from django.urls import path
from . import views

urlpatterns = [
    path('Customers_Mng/', views.Customer, name='Customers_Mng'),
]