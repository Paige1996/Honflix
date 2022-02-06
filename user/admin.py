from django.contrib import admin
from .models import UserModel, WishList

# Register your models here.
admin.site.register(UserModel)
admin.site.register(WishList)