from django.db import models
from core import models as core_models

# Create your models here.
class Iostream(core_models.TimeStampedModel):
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    text = models.TextField(null=False)
    reply_to = models.ForeignKey("self", null=True, blank="True", on_delete=models.CASCADE, related_name= "replies")
    file = models.ImageField(upload_to="uploads/iostreamç", blank="True", null="True")

    def __str__(self):
        return self.text