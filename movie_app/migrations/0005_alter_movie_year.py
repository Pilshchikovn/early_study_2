# Generated by Django 4.1 on 2022-08-21 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0004_movie_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
