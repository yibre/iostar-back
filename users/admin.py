from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    """ Custom User Admin """

    list_display = ("school_email", "gender", "school", "language", "student_id", "email_verified", "email_secret")
    list_filter = ("language", "school", "student_id")
    search_fields = ('school_email', 'school',)