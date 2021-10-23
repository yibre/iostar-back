from django.db import models
from core import models as core_models

class List(core_models.TimeStampedModel):

    """
    This is to show fav post lists for users, each user can have one fav lists
    """

    # list owner
    name = models.CharField(max_length=80)
    owner = models.ForeignKey("users.User", related_name="lists", on_delete=models.CASCADE)
    posts = models.ManyToManyField("posts.Post", related_name="lists", blank=True)

    def __str__(self):
        return self.name

    def count_posts(self):
        return self.posts.count()

    count_posts.short_description = "Number of posts"


class FavBand(core_models.TimeStampedModel):
    owner = models.ForeignKey("users.User", related_name="favbands", on_delete=models.CASCADE)
    band = models.ManyToManyField("bands.Band", related_name="favbands", blank=True)