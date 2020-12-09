from django.contrib import admin
from django.urls import path
from account import views

urlpatterns = [
    path('', views.Home,name='home'),
    path('orders/', views.Orders,name='orders'),
    path('help/', views.Help,name='help'),
]
