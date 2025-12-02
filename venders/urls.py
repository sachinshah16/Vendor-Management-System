from django.contrib import admin
from django.urls import path
from venders import views

urlpatterns = [
    path('venderregister', views.venderRegister, name='venderregister'),
    path('<int:id>', views.vender_details, name='venderdetails'),
    path('addfood', views.addFood, name='addfood')
   
]