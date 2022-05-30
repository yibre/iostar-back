from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

app_name = "comments"

urlpatterns = [
    path('<int:id>/delete', views.comment_delete, name="comment_delete"),
]