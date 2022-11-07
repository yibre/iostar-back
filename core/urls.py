from bands.models import Band
from django.urls import path
from core.views import resolve_home

app_name = "core"

urlpatterns = [
    path("", resolve_home, name="home"),
]