# Generated by Django 4.0.5 on 2022-06-21 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_customerrequest_assigned_to'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='requeststatus',
            options={'ordering': ['status'], 'verbose_name_plural': 'Request Statuses'},
        ),
    ]
