from django import forms
from . import models
from bands.models import models as Band

class PostForm(forms.Form):

    class Meta:
        model = models.Post
        
    def save(self, *args, **kwargs):
        post =  super().save(commit=False)


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')    
    class Meta:
        model = models.Images
        fields = ('image', )