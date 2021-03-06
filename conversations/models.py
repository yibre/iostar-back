from django.db import models
from core import models as core_models
# Create your models here.

class Conversation(core_models.TimeStampedModel):

    """Conversation between users in a certain groups"""

    participants = models.ManyToManyField(
        "users.User", related_name="converstation", blank=True
    )

    def __str__(self):
        return str(self.created)

class Message(core_models.TimeStampedModel):
    """ Message Model Definition """

    message = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    conversation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} says: {self.text}"