# Generated by Django 2.2.6 on 2020-06-07 12:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=20)),
                ('slug', models.CharField(max_length=300)),
                ('likes', models.ManyToManyField(blank=True, default=None, related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]