from django.contrib import admin
from django.utils.html import mark_safe
from . import models

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    """ Post Admin Definition """

    list_display = ('title', 'author', 'band')
    search_fields = ('title',)


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Photo Admin Definition """
    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"

@admin.register(models.Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ("title", "get_thumbnails")
    search_fields = ('title',)


@admin.register(models.Twinkle)
class TwinkleAdmin(admin.ModelAdmin):
    list_display = ("__str__", 'author')