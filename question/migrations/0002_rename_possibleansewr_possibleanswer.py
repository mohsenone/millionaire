# Generated by Django 3.2.5 on 2021-07-29 21:04

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0001_initial'),
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PossibleAnsewr',
            new_name='PossibleAnswer',
        ),
    ]
