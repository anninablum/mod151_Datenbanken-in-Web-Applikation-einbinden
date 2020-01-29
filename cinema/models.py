from django.db import models

# Create your models here.

TITLES = (
    ('Dr.', 'Dr'),
    ('Mr.', 'Mr'),
    ('Mrs.', 'Mrs'),
    ('Ms.', 'Ms'),
)


class Movie(models.Model):
    movie_title = models.CharField(max_length=30)
    movie_genre = models.CharField(max_length=30)
    length = models.IntegerField()
    age_restriction = models.IntegerField()

    def __str__(self):
        return '%s %s' % (self.movie_title, self.length)


class Customer(models.Model):
    title = models.CharField(max_length=4, choices=TITLES)
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Cinema(models.Model):
    cinema_title = models.CharField(max_length=50)
    location = models.CharField(max_length=50)


# class MovieList(models.Model):
#     fk_cinema = models.ManyToManyField(Cinema)
#     fk_movie = models.ManyToManyField(Movie)


# class TicketRegistration(models.Model):
#     fk_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     fk_movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
