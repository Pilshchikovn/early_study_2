# Generated by Django 4.1 on 2022-08-20 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_movie_budget_movie_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
