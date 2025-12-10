from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registration, name='register'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('edit/',views.update, name='update')
]