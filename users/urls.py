from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.log_out, name="logout"),
    path("signup", views.SignUpView.as_view(), name="signup"),
    path("editprofile", views.EditProfileView.as_view(), name="edit-profile"),
    path("verify/<str:key>", views.complete_verification, name="complete-verification"),
    path("<int:pk>/", views.UserProfileView.as_view(), name="profile"),
]