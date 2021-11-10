from django import forms
from django.forms.fields import EmailField
from django.shortcuts import render
from . import models

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))


class SignUpForm(forms.Form):
    
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    schoolEmail = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    schoolmail_list = ["kaist.ac.kr", "dgist.ac.kr", "unist.ac.kr", "gist.ac.kr"]

    def clean_email(self): # email이 valid 한지 고민해야함
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError("User already exists with that email")
        except models.User.DoesNotExist:
            return email
        
    def clean_schoolEmail(self):
        schoolEmail = self.cleaned_data.get("schoolEmail")
        print(schoolEmail)
        for maillist in ["kaist.ac.kr", "dgist.ac.kr", "unist.ac.kr", "gist.ac.kr"]:
            if maillist in schoolEmail:
                print("yes we found it!")
                return schoolEmail
        print("we didn't find any school name")
        raise forms.ValidationError("Email without school email")

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password != password1:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return password


    def save(self):
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        schoolEmail = self.cleaned_data.get("schoolEmail")

        # DY edit: school email에 따른 school 옵션 추가하는 함수

        user = models.User.objects.create_user(email, password, schoolEmail, first_name, last_name) # 이게 유저를 만들어줌
        user.first_name=first_name
        user.last_name = last_name


    """
    현 진행 상태:
    create_user에서 3 positional argument가 들어가야하는데 5개 주어졌다고 찡찡대는 중
    이부분 고쳐야 함
    """