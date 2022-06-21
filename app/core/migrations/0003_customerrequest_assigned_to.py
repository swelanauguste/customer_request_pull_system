# Generated by Django 4.0.5 on 2022-06-21 12:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_requeststatus_alter_customerrequest_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerrequest',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
