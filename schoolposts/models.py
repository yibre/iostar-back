from django.db import models
from posts import models as post_models
from users import models as user_models
# Create your models here.

from django.template.defaultfilters import slugify

# 출처: https://stackoverflow.com/questions/34006994/how-to-upload-multiple-images-to-a-blog-post-in-django

class SchoolPost(post_models.Post):
    SCHOOL_DGIST = "dgist"
    SCHOOL_KAIST = "kaist"
    SCHOOL_UNIST = "unist"
    SCHOOL_GIST = "gist"
    SCHOOL_POSTECH = "postech"
    SCHOOL_OTHERS = "others"

    SCHOOL_CHOICES = (
        (SCHOOL_DGIST, "DGIST"),
        (SCHOOL_KAIST, "KAIST"),
        (SCHOOL_UNIST, "UNIST"),
        (SCHOOL_GIST, "GIST"),
        (SCHOOL_POSTECH, "POSTECH"),
        (SCHOOL_OTHERS, "OTHER")
    )
    School = models.CharField(
        choices = SCHOOL_CHOICES, null=True, blank=True, default="", max_length=20,
    )

class KaistPost(SchoolPost):
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
