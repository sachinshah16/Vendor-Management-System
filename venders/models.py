from django.db import models
from django.conf import settings


# Create your models here.

class multiVenders(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    
    restaurent_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    restaurent_lic = models.ImageField(upload_to='licience_pics', blank=True, null=True)
    restaurent_img = models.ImageField(upload_to='restaurent_pics', blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    user_type = models.CharField(max_length=100, default='vender', editable=False)

    def __str__(self):
        return self.user.username

class foodItem(models.Model):
    vender = models.ForeignKey(multiVenders, on_delete=models.CASCADE, related_name='food_items')
    food_name = models.CharField(max_length=50)
    food_desc = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    food_img = models.ImageField(upload_to='foodimg', blank=True, null=True)
    
    def __str__(self):
        return self.food_name


