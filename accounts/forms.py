from django import forms
from accounts.models import userDetails
from django.contrib.auth.models import User
from django_recaptcha.fields import ReCaptchaField


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username','email','password']

class userFormDetails(forms.ModelForm):
    class Meta:
        model = userDetails
        fields = ['phone', 'house_no','street','city','state','zipcode','img'] 
    captcha = ReCaptchaField()

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email"]

class UpdateUserProfileform(forms.ModelForm):
    class Meta:
        model=userDetails
        fields=["phone","house_no","street","city","state","zipcode","img"]