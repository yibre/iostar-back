from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Iostream)
class TwinkleAdmin(admin.ModelAdmin):
    list_display = ("__str__", 'author')