from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    director_email = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name} '

    def get_url(self):
        return reverse('one_director', args=[self.id])


class Movie(models.Model):
    Currencey_choices = [
        ('e', 'Euro'),
        ('d', 'Dolar'),
        ('r', 'Ruble'),

    ]
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=1000000)
    slug = models.SlugField(default='', null=False, db_index=True)
    currency = models.CharField(max_length=1, choices=Currencey_choices, default='r')
    director = models.ForeignKey(Director, on_delete=models.PROTECT, null=True)

    # director = models.ForeignKey(Director, on_delete=models.CASCADE,null=True)
    # director = models.ForeignKey(Director, on_delete=models.SETNULL,null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - рейтинг {self.rating} '

    def get_url(self):
        return reverse('movie-detail', args=[self.slug])
