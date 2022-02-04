from django.contrib import admin
from .models import ContentModel, Category

# Register your models here.
admin.site.register(ContentModel)
admin.site.register(Category)