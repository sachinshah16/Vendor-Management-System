from django.db import models
from django.conf import settings
from venders.models import foodItems

# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class cartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey(foodItems, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
