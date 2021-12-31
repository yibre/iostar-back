from django import forms
from . import models
from bands.models import Band

class UploadAdForm(forms.ModelForm):
    """ 홍보용 게시글을 등록하기 위한 사이트 """
    class Meta:
        model = models.Post
        fields = (
            "title",
            "content",
        )
    
    # author = models.users

    def save(self, *args, **kwargs):
        post = super().save(commit=False)
        band = Band.objects.get(name="promotions")
        post.band = band
        post.save()


class PhotoForm(forms.ModelForm):
    photo = forms.ImageField(label="Image")
    class Meta:
        model = models.Photo
        fields = ('photo', )