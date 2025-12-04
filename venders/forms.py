from django import forms
from venders.models import multiVenders, foodItem
from django.contrib.auth import get_user_model


User = get_user_model()


class venderForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username','email','password']

class venderDetailsForm(forms.ModelForm):
    class Meta:
        model = multiVenders
        fields = '__all__'
        exclude = ('is_approved', 'user_type', 'user')

class UpdateVenderForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email"]

class UpdateVenderDetailsform(forms.ModelForm):
    class Meta:
        model=multiVenders
        fields = '__all__'
        exclude = ('is_approved', 'user_type', 'user')

class addFoodForm(forms.ModelForm):
    class Meta:
        model = foodItem
        fields = '__all__'
        exclude = ('vender',)
    
    