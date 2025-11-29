from django.shortcuts import render
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
    return render(request, 'venders/vender_details.html',{'vender':vender})


