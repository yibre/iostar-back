from django import forms
from django.forms.fields import EmailField
from django.shortcuts import render
from . import models

class LoginForm(forms.Form):
    required_css_class = 'required-field'
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        # 폼 안에 class를 만들어주는 역할
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'email@example.com'
        self.fields['password'].widget.attrs['placeholder'] = 'password'
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

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


class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("first_name", "last_name", "email", "email_2nd", "stutus")

    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    schoolmail_list = ["kaist.ac.kr", "dgist.ac.kr", "unist.ac.kr", "gist.ac.kr"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        return email
        for maillist in ["kaist.ac.kr", "dgist.ac.kr", "unist.ac.kr", "gist.ac.kr"]:
            if maillist in email:
                return email
        raise forms.ValidationError("Email should include 'kaist.ac.kr', 'dgist.ac.kr', 'unist.ac.kr', 'gist.ac.kr'")

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
        if "kaist" in email:
            user.school = "kaist"
        elif "dgist" in email:
            user.school= "dgist"
        elif "unist" in email:
            user.school= "unist"
        elif "gist" in email:
            user.school= "gist"
        elif "postech" in email:
            user.school= "postech"
        password = self.cleaned_data.get("password")
        user.set_password(password)
        user.username = email
        user.save()

    def __init__(self, *args, **kwargs):
        # 폼 안에 class를 만들어주는 역할
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['email_2nd'].widget.attrs['placeholder'] = 'email@example.com'
        self.fields['password'].widget.attrs['placeholder'] = 'password'
        self.fields['password1'].widget.attrs['placeholder'] = 'repeat password '
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'