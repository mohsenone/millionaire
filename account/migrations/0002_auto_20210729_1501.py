# Generated by Django 3.2.5 on 2021-07-29 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='surname',
            field=models.CharField(blank=True, max_length=50, verbose_name='Surname'),
        ),
    ]