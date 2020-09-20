from app.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("real_name")
        parser.add_argument("time_zone", choices=["USA/LA", "AS/WB"])

    def handle(self, *args, **options):
        user = User(
            real_name=options["real_name"],
            time_zone=options["time_zone"]
        )
        user.save()
        self.stdout.write(self.style.SUCCESS("Successfully added!."))