from django.contrib import admin
from . import models

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    """ Post Admin Definition """

    list_display = ('title', 'author', 'band')
    search_fields = ('title',)


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Photo Admin Definition """
    pass