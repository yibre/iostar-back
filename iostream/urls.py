from django.urls import path
from . import views

app_name = "iostream"

urlpatterns = [
    path("", views.IostreamListView.as_view(), name="main"),
    path("uploads/", views.IostreamListView.as_view(), name="upload"),
    # Todo: delete 기능 추가하기! edit 기능은 만들지 말기
]

