from django.contrib import admin
from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# Register your models here.

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    """post admin definition"""

    list_display = ('user', 'title',)
    search_fields = ('title',)

@admin.register(models.Images)
class ImagesAdmin(admin.ModelAdmin):
    """image admin definition"""

    list_display = ('post',)
