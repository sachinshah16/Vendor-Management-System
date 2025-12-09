from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from venders.models import *
from venders.forms import *
from accounts.decorator import *


# Create your views here.
@logout_required
def venderRegister(request):
    registerd = False

    if request.method == 'POST':
        user_form = venderForm(request.POST)
        details_form = venderDetailsForm(request.POST, request.FILES)

        if user_form.is_valid() and details_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            details = details_form.save(commit=False)
            details.user = user
            details.save()
            registerd = True
    else:
        user_form = venderForm()
        details_form = venderDetailsForm()
    
    return render(request, 'venders/vender_register.html', {'form1':user_form,'form2':details_form, 'registerd':registerd})

def vender_details(request, id=0):
    vender = multiVenders.objects.get(id=id)
    fooditems = vender.food_items.all()
    return render(request, 'venders/vender_details.html',{'vender':vender,'fooditems':fooditems})

@login_required(login_url='login')
def addMenu(request):
    get_object_or_404(multiVenders, user=request.user)

    if request.method == "POST":
        form = addFoodForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.vender = request.user.multivenders
            item.save()
            return redirect('dashboard')
            
    else:
        form = addFoodForm()
    return render(request, 'venders/addmenu.html', {'form':form})

@login_required(login_url='login')
def vender_profile_update(request):
    get_object_or_404(multiVenders, user=request.user)

    form = UpdateVenderForm(instance=request.user)
    form1=UpdateVenderDetailsform(instance=request.user.multivenders)
    if request.method=="POST":
        form=UpdateVenderForm(request.POST,request.FILES,instance=request.user)
        form1=UpdateVenderDetailsform(request.POST,request.FILES,instance=request.user.multivenders)
        if form.is_valid() and form1.is_valid():
            user=form.save()
            profile=form1.save(commit=False)
            profile.user=user
            profile.save()

            return redirect("dashboard")
    return render(request,"venders/vender_update.html",{"form1":form,"form2":form1})

@login_required(login_url='login')
def editFoodItem(request, id):
    get_object_or_404(multiVenders, user=request.user)

    vender = request.user.multivenders
    food_item = get_object_or_404(vender.food_items,id=id)
    form = editFoodForm(instance=food_item)

    if request.method == 'POST':
        form = editFoodForm(request.POST, request.FILES, instance=food_item)

        if form.is_valid():
            form.save()
            return redirect('dashboard')


    return render(request, 'venders/edit_food_item.html',{'form':form})   


@login_required(login_url='login')
@require_POST
def deleteFoodItem(request, id):
    
    vendor = request.user.multivenders
    # food = vendor.food_items.get(id = id)
    food = get_object_or_404(foodItems, id=id, vender=vendor)
    food.delete()
    return redirect('dashboard')

