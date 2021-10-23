from django import forms
from . import models
from bands import models as Band

class uploadAdFrom(forms.Form):
    """ 홍보용 게시글을 등록하기 위한 사이트 """
    # 아직 작업 다 안 끝남!!! class meta부터 전부 수정해야됨.
    class Meta:
        model = models.Post
        fields = (
            "title",
            "contents",
            "country",
        )

    band = Band.objects.filter(name="promotions") # 이게 먹힐지 잘 모르겠음
    author = models.users

    def save(self, *args, **kwargs):
        post = super().save(commit=False)
        return post