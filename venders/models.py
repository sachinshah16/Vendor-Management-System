from django.db import models
from django.conf import settings


# Create your models here.

class multiVenders(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,        
        blank=True,
    )

    vender_name = models.CharField(max_length=100)
    restaurent_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    restaurent_lic = models.ImageField(upload_to='licience_pics', blank=True, null=True)
    restaurent_img = models.ImageField(upload_to='restaurent_pics', blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    user_type = models.CharField(max_length=100, default='vender')

    def __str__(self):
        return self.restaurent_name

