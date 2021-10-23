from django.core.management.base import BaseCommand
from django_seed import Seed
from bands.models import Band

class Command(BaseCommand):
    
    help = "this command is for creating new users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many users you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} users created!"))