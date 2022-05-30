from django import forms
from . import models
from bands.models import Band
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django_ckeditor_5.widgets import CKEditor5Widget


class UploadAdForm(forms.ModelForm):
    """ 홍보용 게시글을 등록하기 위한 사이트 """
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = models.Post
        fields = (
            "title",
            "content",
        )
    
    # author = models.users

    def __init__(self, *args, **kwargs):
        # 폼 안에 class를 만들어주는 역할
        super(UploadAdForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = '제목'
        self.fields['content'].widget.attrs['placeholder'] = '내용 /n 어쩌고저쩌고 기타등등'
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'post_form'
        self.fields['content'].widget.attrs['class'] = 'content_input'


    def save(self, *args, **kwargs):
        post = super().save(commit=False)
        return post



class PhotoForm(forms.ModelForm):
    photo = forms.ImageField(label="Image")
    class Meta:
        model = models.Photo
        fields = ('photo', )