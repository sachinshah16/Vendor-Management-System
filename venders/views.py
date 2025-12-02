from django.shortcuts import render, redirect
from venders.models import *
from venders.forms import *

# Create your views here.
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
    fooditems = foodItem.objects.filter(vender = id)
    return render(request, 'venders/vender_details.html',{'vender':vender,'fooditems':fooditems})

def addFood(request):
    msg = ''
    if request.method == "POST":
        form = addFoodForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.vender = request.user.multivenders
            item.save()
            msg = "Item added successfuly"
            redirect('addfood')
            
    else:
        form = addFoodForm()
    return render(request, 'venders/addfood.html', {'form':form, 'msg':msg})



