# Generated by Django 4.1 on 2022-08-21 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0006_movie_director'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director_email',
            field=models.CharField(default='sugardaddy@gmail.com', max_length=100),
        ),
    ]
