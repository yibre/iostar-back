from django.db import models
from core import models as core_models
from users import models as user_models

class BandMember(core_models.TimeStampedModel):
    """the list of members in the group"""
    members = models.ManyToManyField(user_models.User)

    class Meta:
        verbose_name = "Band Member"

class Band(core_models.TimeStampedModel):
    
    """Group Model: make a group, modify a group setting, add schedule"""

    GROUPTYPE_SCHOOL = "학교행정"
    GROUPTYPE_COURSES = "과목"
    GROUPTYPE_CLUB = "동아리"
    GROUPTYPE_OTHERS = "기타"

    GROUPTYPE_CHOICES = (
        (GROUPTYPE_SCHOOL, "학교행정"),
        (GROUPTYPE_COURSES, "과목"),
        (GROUPTYPE_CLUB, "동아리"),
        (GROUPTYPE_CLUB, "기타"),
    )

    name = models.CharField(max_length=140)
    # is it official group or not
    members = models.ForeignKey("BandMember", on_delete=models.CASCADE)
    official = models.BooleanField(default=False)
    grouptype = models.CharField(choices=GROUPTYPE_CHOICES, max_length=20, null=True)
    definition = models.TextField(blank=True, null=True)
    chairperson = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True, related_name='%(class)s_chairman')
    mainfile = models.ImageField(blank = True, null=True)
    bannerfile = models.ImageField(blank = True, null=True)
    
    def count_members(self, obj):
        return obj.members.count()

    def __str__(self):
        return self.name

"""
on delete options
https://lee-seul.github.io/django/backend/2018/01/28/django-model-on-delete.html
"""