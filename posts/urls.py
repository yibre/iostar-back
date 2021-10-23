from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("ads/uploads/", views.UploadAdView.as_view(), name="ad_uploads"),
    path("ads/<int:ads_pk>/delete/", views.ad_delete, name="ad_delete"),
    path("ads/<int:ads_pk>/edit/", views.ad_edit, name="ad_edit"),
]