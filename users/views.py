from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect, reverse
from django.contrib.auth import authenticate, login, logout
from . import forms

class LoginView(FormView):
    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home") # 당장 함수를 부르지 않음

    def form_valid(self, form):
        school_email = form.cleaned_data.get("school_email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=school_email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

class SignUpView(FormView):

    template_name = "users/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("core:home")
    initial = {"first_name": "Nicoas", "last_name": "Serr", "email": "itn@las.com"}

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        school_email = form.cleaned_data.get("school_email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=school_email, email = email, password=password)
        if user is not None:
            login(self.request, user)
        user.verify_email()
        return super().form_valid(form)

def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))

    # 15.3 강의 듣는 중