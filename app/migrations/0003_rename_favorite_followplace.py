# Generated by Django 5.1.1 on 2024-11-15 07:25

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_favoirite_user_favorite_favorite_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Favorite',
            new_name='FollowPlace',
        ),
    ]
