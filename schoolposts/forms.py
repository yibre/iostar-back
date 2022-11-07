from django import forms
from . import models
from .models import SchoolPost
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

 
class UploadPostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = models.SchoolPost
        fields = (
            "title",
            "content",
        )

    def __init__(self, *args, **kwargs):
        # 폼 안에 class를 만들어주는 역할
        print("hello thisis come from upload post form")
        super(UploadPostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = '제목'
        self.fields['content'].widget.attrs['placeholder'] = '내용 /n 어쩌고저쩌고 기타등등'
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'post_form'
        self.fields['content'].widget.attrs['class'] = 'content_input'

    def save(self, *args, **kwargs):
        post = super().save(commit=False)
        return post