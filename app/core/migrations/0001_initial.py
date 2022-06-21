# Generated by Django 4.0.5 on 2022-06-21 12:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=100)),
                ('customer_email', models.EmailField(max_length=254, verbose_name='email')),
                ('customer_telephone', models.CharField(help_text='468-5050 or 456-5050', max_length=20)),
                ('customer_name', models.CharField(max_length=254, verbose_name='name')),
                ('customer_department', models.CharField(max_length=254, verbose_name='department')),
                ('desc', models.TextField(verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ministry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('ministry_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerRequestComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='core.customerrequest')),
            ],
        ),
        migrations.AddField(
            model_name='customerrequest',
            name='customer_ministry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ministry'),
        ),
    ]
