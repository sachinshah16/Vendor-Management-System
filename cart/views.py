from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, cartItems
from venders.models import foodItems

# Create your views here.
def DisplayCart(request):
    cart = request.user.cart
    cart_items = cart.items.all()

    subtotal = 0

    for item in cart_items:
        subtotal += item.item.price * item.quantity

    
    tax = float(subtotal)*0.12
    del_fee = 5*len(cart_items)
    grandtotal = float(subtotal) + tax + del_fee
    
    return render(request,'cart.html',{'cart_items':cart_items,'subtotal':subtotal,'tax':round(tax,2),'delivery_fee':del_fee,'grandtotal':round(grandtotal,2)})

def addToCart(request, item_id):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    food = get_object_or_404(foodItems, id=item_id)

    cart_item, created = cartItems.objects.get_or_create(cart=cart, item=food)

    if not created:
        cart_item.quantity += 1

    cart_item.save()

    v_id = food.vender.id
    print(v_id)
    return redirect('venderdetails',v_id)

def changeQuantity(request,id):
    if request.method == 'POST':
        data = request.POST.get('quantity')
        cart = request.user.cart
        item = cart.items.get(id=id)
        item.quantity = data
        item.save()
        return redirect('cart')

def removeFromCart(request, id):
    cart = request.user.cart
    it = cart.items.get(id=id)
    it.delete()
    return redirect('cart')