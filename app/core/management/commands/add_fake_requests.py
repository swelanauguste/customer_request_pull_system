import random

from django.core.management.base import BaseCommand
from faker import Faker
from users.models import User

from ...models import CustomerRequest, Ministry


class Command(BaseCommand):
    help = "Add faker data to the database"

    def handle(self, *args, **kwargs):
        # CustomerRequest.objects.all().delete()
        fake = Faker()
        # print(fake.word(ext_word_list=['accounts', 'administration', 'general']))
        for _ in range(500):
            customer_email = fake.email()
            customer_telephone = fake.phone_number()
            customer_name = fake.name()
            customer_ministry = Ministry.objects.get(pk=random.randint(1, 4))
            customer_department = fake.word(
                ext_word_list=["accounts", "administration", "general"]
            )
            desc = fake.paragraph(nb_sentences=6)
            CustomerRequest.objects.get_or_create(
                customer_email=customer_email,
                customer_telephone=customer_telephone,
                customer_name=customer_name,
                customer_ministry=customer_ministry,
                customer_department=customer_department,desc=desc
            )
