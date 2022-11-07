from django.contrib import admin
from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# Register your models here.

@admin.register(models.SchoolPost)
class SchoolPostAdmin(admin.ModelAdmin):
    """post admin definition"""
    list_display = ('band', 'author',)