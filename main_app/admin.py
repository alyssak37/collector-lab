from django.contrib import admin
from .models import Icecream, Eating, Topping, Photo
# Register your models here.

admin.site.register(Icecream)
admin.site.register(Eating)
admin.site.register(Topping)
admin.site.register(Photo)