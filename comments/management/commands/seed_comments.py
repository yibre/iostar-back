from django.core.management.base import BaseCommand
from django_seed import Seed
import random
from users import models as user_models
from posts import models as post_models
from comments import models as comment_models

class Command(BaseCommand):
    
    help = "this command is for creating new comments"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many comments you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_posts = post_models.Post.objects.all()
        all_users = user_models.User.objects.all()
        seeder.add_entity(
            comment_models.Comment,
            number,
            {
                "writer": lambda x: random.choice(all_users),
                "post": lambda x: random.choice(all_posts),
            }
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} comments created!"))