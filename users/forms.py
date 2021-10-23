from django import forms
from django.shortcuts import render
from . import models

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email=self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            return email
        except models.User.DoesNotExist:
            raise forms.ValidationError("User does not exist")

    def clean_password(self): # clean method는 데터ㄹ return 해야함
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password): # 해당 함수가 유저의 password를 체크하는 함수임
                return password
            else:
                raise forms.ValidationError("Password is wrong")
        except models.User.DoesNotExist:
            pass
        # password를 확인하기 위해 가장 먼저 해야 할 일: 유저 확인하기


class SignUpForm(forms.Form):
    
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    # 14.3 강의 하는 중
    """
    현 진행 상태: 유저 이름을 넣으면 유저의 정보를 확인하는 것까지는 진행 완료
    
    """