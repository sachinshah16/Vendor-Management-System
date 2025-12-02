from django.contrib import admin

# Register your models here.

from .models import multiVenders, foodItem

admin.site.register(multiVenders)
admin.site.register(foodItem)


