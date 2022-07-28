from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


app_name = "posts"

urlpatterns = [
    path("promotions/", views.PromotionListView.as_view(), name="promotions"),
    path("promotions/<int:pk>", views.PromotionDetailView.as_view(), name="promotion_detail"),
    path("promotions/uploads/", views.UploadAdView.as_view(), name="promotion_uploads"),
    path("<int:pk>/delete/", views.post_delete, name="post_delete"),
    path("<int:pk>/edit/", views.EditPostView.as_view(), name="edit"),
    path("search/", views.search, name="search"),
    path("hobby/", views.HobbyHome.as_view(), name= "hobby"),
    path("life/", views.SchoolLife.as_view(), name="school"),
    path("career/", views.CareerHome.as_view(), name="career"),
    path("notice/", views.NoticeView.as_view(), name="iostar-notice"),
    path("notice/uploads/", views.NoticeView.as_view(), name="iostar-notice"),
    path("notice/<int:pk>", views.PromotionDetailView.as_view(), name="notice_detail"),
    path("<str:band_title>/uploads/", views.UploadView.as_view(), name="post_upload"),
    path("<str:band_title>/<int:pk>", views.PostDetailView.as_view(), name="post_detail"),
]

def protected_file(request, path, document_root=None):
    # 파일 경로를 통ㅐ 파일에 직접 접근하지 못하게 막는 코드
    # 출처: https://parkhyeonchae.github.io/2020/04/13/django-project-25/
    messages.error(request, "접근 불가")
    return redirect('/')