from django import forms
from django.forms.fields import EmailField
from django.shortcuts import render
from . import models

class LoginForm(forms.Form):
    school_email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        school_email = self.cleaned_data.get("school_email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(school_email=school_email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))
        except models.User.DoesNotExist:
            self.add_error("school_email", forms.ValidationError("User does not exist"))


class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("first_name", "last_name", "school_email", "email","stutus")

    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    schoolmail_list = ["kaist.ac.kr", "dgist.ac.kr", "unist.ac.kr", "gist.ac.kr"]

    def clean_schoolEmail(self):
        school_email = self.cleaned_data.get("school_email")
        for maillist in ["kaist.ac.kr", "dgist.ac.kr", "unist.ac.kr", "gist.ac.kr"]:
            if maillist in school_email:
                return school_email
        print("we didn't find any school name")
        raise forms.ValidationError("Email without school email")

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password != password1:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return password


    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        schoolEmail = self.cleaned_data.get("schoolEmail")
        user.set_password(password)
        user.username = schoolEmail
        user.email = email
        user.schoolEmail = schoolEmail
        user.set_password(password)
        user.save()

    """
    현 진행 상태: mail verification 기능 만드는 중
    
    """