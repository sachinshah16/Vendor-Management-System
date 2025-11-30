from django import forms
from venders.models import multiVenders
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
    