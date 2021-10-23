from django.core.management.base import BaseCommand
from django_seed import Seed
import random
from django.contrib.admin.utils import flatten
from users import models as user_models
from posts import models as post_models
from lists import models as list_models

NAME = "lists"

class Command(BaseCommand):
    
    help = f"This command creates {NAME}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many comments you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        posts = post_models.Post.objects.all()
        users = user_models.User.objects.all()
        seeder.add_entity(
            list_models.List,
            number,
            {
                "owner": lambda x: random.choice(users)
            }
        )
        created = seeder.execute()
        cleaned = flatten(list(created.values()))
        for pk in cleaned:
            list_model = list_models.List.objects.get(pk=pk)
            # 랜덤한 포스트의 리스트를 얻고자 함
            to_add = posts[random.randint(0, 5) : random.randint(6, 30)]
            list_model.posts.add(*to_add)

        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created!"))