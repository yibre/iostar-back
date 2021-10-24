from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect, reverse, render
from django.contrib.auth import authenticate, login, logout
from . import forms

class LoginView(FormView):
    def get(self, request):
        form = forms.LoginForm(initial={"email": "itn@las.com"})
        return render(request, "users/login.html",  {"form": form})
    
    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                print("login succeess")
                login(request, user)
                return redirect(reverse("core:home"))
        return render(request, "users/login.html",  {"form": form})

class SignUpView(FormView):
    pass

def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))