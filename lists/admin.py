from django.contrib import admin
from . import models


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):

    """ List Admin Definition """

    list_display = ("name", "owner", "count_posts")

    search_fields = ("name",)

    filter_horizontal = ("posts",)