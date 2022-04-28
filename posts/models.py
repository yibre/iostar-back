from django.db import models
from core import models as core_models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django_ckeditor_5.fields import CKEditor5Field
from ckeditor_uploader.fields import RichTextUploadingField

class Photo(core_models.TimeStampedModel):

    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    post = models.ForeignKey("Post", related_name = "photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
# 여러가지 photo가 하나의 게시글에 연관지어질 수 있음.

class Post(core_models.TimeStampedModel):
    
    """Post Model: each group can have a boards, a list of memos"""
    band = models.ForeignKey("bands.Band", on_delete=models.CASCADE, related_name="posts")
    author = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="posts")
    content = RichTextUploadingField(blank=True, null=True)
    # content = CKEditor5Field('Content', config_name= 'extends', blank=True, null=True)
    #content = models.TextField(null=False)
    title = models.CharField(max_length=100, null=False)
    modified_date = models.DateTimeField(auto_now=True) # 마지막 수정일자
    heart = models.IntegerField(default=0) # 게시글에 좋아요 한 횟수
    views = models.IntegerField(default=0) # 게시글 조회수

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"pk": self.pk})

    def first_photo(self):
        try:
            photo, = self.photos.all()[:1]
            return photo.file.url
        except ValueError:
            return None
    
    def get_all_photo(self):
        try:
            photo, = self.photos.all()
            return photo.file.url
        except ValueError:
            return None
    
    def delete(self, *args, **kwargs):
        if self.get_all_photo:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.upload_files.path))
        super(Post, self).delete(*args, **kargs)


class Notice(Post):
    """ iostar notice post for homepage 
    홈페이지 메인에 실을 화면이 필요해서 만듦 """
    homepage = models.BooleanField(default=False) #true면 홈페이지에 실음, 아니면 안실음
    thumbnail_image = models.ImageField(upload_to='featured_image/%Y/%m/%d/')
    
    def get_thumbnails(self):
        try:
            return self.thumbnail_image.url
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