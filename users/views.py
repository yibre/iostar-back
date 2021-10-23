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
            print(form.cleaned_data)
        return render(request, "users/login.html",  {"form": form})

class SignUpView(FormView):
    pass

def log_out():
    pass