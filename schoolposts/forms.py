from django import forms
from . import models
from bands.models import models as Band

class UploadPostForm(forms.Form):

    def save(self, *args, **kwargs):
        post =  super().save(commit=False)