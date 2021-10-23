from django.urls import path
from . import views

app_name = "band"

urlpatterns = [
    path("<int:pk>", views.BandDetail.as_view(), name="detail"), 
]
