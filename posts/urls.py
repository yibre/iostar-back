from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("promotions/", views.PromotionListView.as_view(), name="promotions"),
    path("promotions/<int:pk>", views.PromotionDetailView.as_view(), name="promotion_detail"),
    path("promotions/uploads/", views.UploadAdView.as_view(), name="promotion_uploads"),
    path("promotions/<int:ads_pk>/delete/", views.ad_delete, name="promotion_delete"),
    path("promotions/<int:ads_pk>/edit/", views.ad_edit, name="promotion_edit"),
    path("hobby/", views.HobbyHome.as_view(), name= "hobby"),
    path("life/", views.SchoolLife.as_view(), name="school"),
    path("career/", views.CareerHome.as_view(), name="career"),
]