from django.shortcuts import render
from venders.models import *
from venders.forms import *

# Create your views here.
def venderRegister(request):
    registerd = False

    if request.method == 'POST':
        form = venderForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            registerd = True
    else:
        form =  venderForm()
    
    return render(request, 'venders/vender_register.html', {'form':form, 'registerd':registerd})

def vender_details(request, id=0):
    vender = multiVenders.objects.get(id=id)
    return render(request, 'venders/vender_details.html',{'vender':vender})


