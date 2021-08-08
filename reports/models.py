from django.db import models
from core import models as core_models
# Create your models here.


# 유저가 댓글 혹은 게시글에 대해 신고하면 comment 혹은 post가 hide 처리됨

class Report(core_models.TimeStampedModel):
    """ This is for reporting comments or posts """

    reporter = models.ForeignKey("users.User", on_delete=models.CASCADE)
    # reporter: 신고자, 관리자 화면에서는 안 나오도록 하기!
    comment= models.ForeignKey("comments.Comment", on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey("post.Post", on_delete=models.CASCADE, null=True, blank=True)