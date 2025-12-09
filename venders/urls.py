from django.contrib import admin
from django.urls import path
from venders import views

urlpatterns = [
    path('register', views.venderRegister, name='venderregister'),
    path('<int:id>', views.vender_details, name='venderdetails'),
    path('addmenu', views.addMenu, name='addmenu'),
    path('update', views.vender_profile_update, name='vender_edit'),
    path('editfooditem/<int:id>', views.editFoodItem, name='editfooditem'),
    path('deletefooditem/<int:id>', views.deleteFoodItem, name='deletefooditem'),
   
]