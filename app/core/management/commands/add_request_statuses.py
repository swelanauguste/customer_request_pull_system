from django.core.management.base import BaseCommand
from faker import Faker
from users.models import User

from ...models import RequestStatus


class Command(BaseCommand):
    help = "Add faker data to the database"

    def handle(self, *args, **kwargs):
        RequestStatus.objects.get_or_create(status="unassigned")
        RequestStatus.objects.get_or_create(status="assigned")
        
       