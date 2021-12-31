from django.db import models
from posts import models as post_models
from users import models as user_models
# Create your models here.

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
