from django import forms
from . import models

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = (
            "comment",
        )

    def __init__(self, *args, **kwargs):
        # 폼 안에 class를 만들어주는 역할
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs['placeholder'] = '댓글을 남기세요'
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'comment_form'

