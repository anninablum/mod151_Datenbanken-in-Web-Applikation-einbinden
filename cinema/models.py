from django.db import models


# Create your models here.


class Customer(models.Model):
    titel = models.CharField(max_length=3)
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=20)
    email = models.EmailField

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Movie(models.Model):
    movie_title = models.CharField(max_length=50)
    length = models.IntegerField
    age_restriction = models.IntegerField

    class Meta:
        ordering = ['movie_title']

    def __str__(self):
        return "%s movie_title" % self.movie_title


class Cinema(models.Model):
    cinema_title = models.CharField(max_length=50)
    location = models.CharField(max_length=50)


class MovieList(models.Model):
    fk_cinema = models.ManyToManyField(Cinema)
    fk_movie = models.ManyToManyField(Movie)


class Registraion(models.Model):
    fk_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    fk_movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
