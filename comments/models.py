from django.db import models
from core import models as core_models

# Create your models here.

class Comment(core_models.TimeStampedModel):
    """ 게시글의 댓글을 관리하기 위한 모델 """
    # 설계: 리뷰와 비슷한 역할을 함. 게시글과 댓글 신고는 어떻게 해야할지 모르겠음.
    comment = models.TextField()
    writer = models.ForeignKey("users.User", on_delete=models.CASCADE)
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE)
    showstatus = models.BooleanField(default=True)
    # 해당 스테이터스가 false일 경우 누군가로부터 신고가 들어왔다는 뜻이며, true인 댓글은 볼 수 있음
    
    def __str__(self):
        return f"{self.comment} - {self.post.title}"

    class Meta:
        ordering = ('-created',)