from django.contrib import admin
from .models import ContentModel, Category, Comment

# Register your models here.
admin.site.register(ContentModel)
admin.site.register(Category)
admin.site.register(Comment)
