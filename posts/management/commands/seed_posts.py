import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from posts import models as post_models
from users import models as user_models
from bands import models as band_models


class Command(BaseCommand):
    
    help = "this command is for creating new posts"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many users you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_bands = band_models.Band.objects.all()
        all_users = user_models.User.objects.all()
        seeder.add_entity(
            post_models.Post,
            number,
            {
                "band": lambda x: random.choice(all_bands),
                "author": lambda x: random.choice(all_users),
            }
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} posts created!"))
        