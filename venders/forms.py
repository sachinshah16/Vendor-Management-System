from django import forms
from venders.models import multiVenders



class venderForm(forms.ModelForm):
    class Meta:
        model = multiVenders
        fields = ['vender_name','restaurent_name','address','city','state','zipcode','restaurent_lic','restaurent_img','is_approved']
    