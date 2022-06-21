from django.core.management.base import BaseCommand
from faker import Faker
from users.models import User

from ...models import Ministry


class Command(BaseCommand):
    help = "Add faker data to the database"

    def handle(self, *args, **kwargs):
        Ministry.objects.get_or_create(ministry="Ministry of Health and Wellness")
        Ministry.objects.get_or_create(ministry="Ministry of Education")
        Ministry.objects.get_or_create(ministry="Ministry of Agriculture")
        Ministry.objects.get_or_create(ministry="Ministry of Tourism")
        
       