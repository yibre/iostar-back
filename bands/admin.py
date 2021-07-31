from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.BandMember)
class BandMemberAdmin(admin.ModelAdmin):
    
    filter_horizontal = ("members",)


@admin.register(models.Band)
class BandAdmin(admin.ModelAdmin):
    
    list_display = (
        "name",
        "grouptype",
        "chairperson"
    )
    # 리스트 디스플레이에서 members의 수를 보여주고 싶은데 어떻게 하지?

    list_filter = ("chairperson", "grouptype")

    search_fields = ("=name", "^chairperson__username")