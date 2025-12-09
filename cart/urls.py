from django.contrib import admin
from django.urls import path
from cart import views

urlpatterns = [
    path('',views.DisplayCart,name='cart'),
    path('add_to_cart/<int:item_id>/',views.addToCart,name='addtocart'),
    path('delete/<int:id>', views.removeFromCart, name='delete'),
    path('change_quantity/<int:id>',views.changeQuantity, name='change_quantity')
]
