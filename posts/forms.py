from django import forms
from . import models
from bands.models import models as Band

class UploadAdForm(forms.Form):
    """ 홍보용 게시글을 등록하기 위한 사이트 """
    # 아직 작업 다 안 끝남!!! class meta부터 전부 수정해야됨.
    class Meta:
        model = models.Post
        fields = (
            "title",
            "contents",
            "file",
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