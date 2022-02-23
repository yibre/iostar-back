from django.db import models
from posts import models as post_models
from users import models as user_models
# Create your models here.

from django.template.defaultfilters import slugify

# 출처: https://stackoverflow.com/questions/34006994/how-to-upload-multiple-images-to-a-blog-post-in-django

class Post(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    body = models.CharField(max_length=400)
  
def get_image_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)  


class Images(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Image')


class KaistPost(post_models.Post):
    # members = user_models.objects.get(school="KAIST")
    pass

# 학교 생활을 위한 class임, 카이스트 학생들만 볼 수 있게.
class Lecture(KaistPost):
    """ 수업별 게시판 """
    pass

class Dorms(KaistPost):
    """ 기숙사 게시판 """
    pass

class Clubs(KaistPost):
    """ 동아리 게시판 """
    pass

class Grades(KaistPost): 
    """ 학년별 게시판 """
    pass

class Majors(KaistPost):
    """ 전공별 게시판 """
    pass
