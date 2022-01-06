from django.urls import path
from . import views

app_name = "schoolposts"

urlpatterns = [
    path("", views.post, name="add-post"),
]