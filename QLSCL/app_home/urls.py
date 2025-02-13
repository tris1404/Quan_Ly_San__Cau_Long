from django.contrib import admin
from django.urls import include, path
from .import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('courts', views.courts, name = "courts"),
    path('court-edit', views.courtEdit, name = "court-edit"),
    path('Customers/', views.Customer, name='Customers'),
]