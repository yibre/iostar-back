from django import forms
from . import models

class UploadIostreamForm(forms.ModelForm):
    """ 홍보용 게시글을 등록하기 위한 사이트 """
    class Meta:
        model = models.Iostream
        fields = (
            "text",
        )
    
    def save(self, *args, **kwargs):
        iostream = super().save(commit=False)
        return iostream