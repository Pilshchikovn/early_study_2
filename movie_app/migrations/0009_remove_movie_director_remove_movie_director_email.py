# Generated by Django 4.1 on 2022-08-21 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0008_director'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='director_email',
        ),
    ]
