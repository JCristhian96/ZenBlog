# Generated by Django 3.2.19 on 2023-05-14 23:28

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0009_auto_20230514_1805'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Favorites',
            new_name='Favorite',
        ),
    ]
