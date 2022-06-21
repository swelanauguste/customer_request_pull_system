# import random

# from django.core.management.base import BaseCommand
# from faker import Faker
# from users.models import User

# from ...models import CustomerRequest, CustomerRequestComment


# class Command(BaseCommand):
#     help = "Add faker data to the database"

#     def handle(self, *args, **kwargs):
#         fake = Faker()
#         # print(fake.word(ext_word_list=['accounts', 'administration', 'general']))
#         for _ in range(500):
#             customer_request = CustomerRequest.objects.get(pk=random.randint(501, 999))
#             comment = fake.paragraph(nb_sentences=2)
#             CustomerRequestComment.objects.get_or_create(
#                 customer_request=customer_request, comment=comment
#             )
