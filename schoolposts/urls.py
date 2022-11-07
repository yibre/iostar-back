from django.urls import path
from . import views

app_name = "schoolposts"

urlpatterns = [
    path("<str:school_name>/main", views.SchoolListView.as_view(), name="home"),
    path("<str:school_name>/<str:band_title>/uploads", views.UploadSchoolPost.as_view(), name="schoolpost_upload"),
    path("<str:school_name>/<str:band_title>/<int:pk>", views.PostDetailView.as_view(), name="schoolpost_detail"),
    path("AllowDenied", views.school_verified_required, name="login-required"),
]