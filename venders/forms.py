from django import forms
from venders.models import multiVenders
from django.contrib.auth.models import User


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
    