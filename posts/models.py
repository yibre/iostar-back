from django.db import models
from core import models as core_models
from django.urls import reverse

class Photo(core_models.TimeStampedModel):

    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
# 여러가지 photo가 하나의 게시글에 연관지어질 수 있음.

class Post(core_models.TimeStampedModel):
    
    """Post Model: each group can have a boards, a list of memos"""
    band = models.ForeignKey("bands.Band", on_delete=models.CASCADE, related_name="posts")
    author = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="posts")
    content = models.TextField(null=False)
    title = models.CharField(max_length=100, null=False)
    modified_date = models.DateTimeField(auto_now=True)
    # 마지막 수정일자
    heart = models.IntegerField(default=0) # 게시글에 좋아요 한 횟수
    views = models.IntegerField(default=0) # 게시글 조회수

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"pk": self.pk})

    def get_photos(self):
        try:
            photo, = self.photos.all()[:1]
            return photo.file.url
        except ValueError:
            return None


class Twinkle(core_models.TimeStampedModel):
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    text = models.TextField(null=False)
    reply_to = models.ForeignKey("self", null=True, blank="True", on_delete=models.CASCADE, related_name= "replies")
    
    def __str__(self):
        return self.text

"""
 장고로 게시판 구현하기
 https://kyuhyuk.kr/article/python/2020/08/15/Django-Board-Post-View
 
"""