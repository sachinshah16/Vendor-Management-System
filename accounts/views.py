from django.shortcuts import render, redirect
from accounts.forms import *
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.models import *
from venders.models import *

# Create your views here.

def registration(request):
    registerd = False
    if request.method == 'POST':
        form1 = UserForm(request.POST)
        form2 = userFormDetails(request.POST, request.FILES)
        
        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            user.set_password(user.password)
            user.save()
            profile = form2.save(commit=False)
            profile.user = user
            profile.save()
            registerd = True
    else:
        form1 = UserForm()
        form2 = userFormDetails()
    return render(request,'registration.html',{'form1':form1,'form2':form2, 'registerd':registerd})

@login_required(login_url="login")
def home(request):
    venders = multiVenders.objects.all()
    return render(request,'index.html',{'venders':venders})

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:

                if hasattr(user, 'userdetails'):
                    role = 'Customer'
                elif hasattr(user, 'multivenders'):
                    role = 'Vender'
                else:
                    role = 'Admin'
                print(role)
                request.session['user_type'] = role
                request.session.save()
                login(request, user)

                return redirect('dashboard')
        else:
            return HttpResponse('<h1>Please check your cred....</h1>')
    return render(request,'login.html',{})


@login_required(login_url="login")
def dashboard(request):
    role = request.session.get('user_type','admin')
    fooditems = foodItem.objects.filter(vender= request.user.multivenders.id)
    return render(request,'dashboard.html',{'role':role, 'fooditems':fooditems})


@login_required(login_url="login")
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def update(request):
    form = UserUpdateForm(instance=request.user)
    form1=UpdateUserProfileform(instance=request.user.userdetails)
    if request.method=="POST":
        form=UserUpdateForm(request.POST,request.FILES,instance=request.user)
        form1=UpdateUserProfileform(request.POST,request.FILES,instance=request.user.userdetails)
        if form.is_valid() and form1.is_valid():
            user=form.save()
            profile=form1.save(commit=False)
            profile.user=user
            profile.save()

            return redirect("dashboard")
    return render(request,"update.html",{"form":form,"form1":form1})
    
    
