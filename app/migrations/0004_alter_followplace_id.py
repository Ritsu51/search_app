# Generated by Django 5.1.1 on 2024-11-15 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_favorite_followplace'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followplace',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
