from django.contrib import admin
from cinema.models import Customer, Movie, Cinema


# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('title', 'first_name', 'last_name', 'email')
    search_fields = ('title', 'first_name', 'last_name', 'email')


admin.site.register(Customer, CustomerAdmin)


class MovieAdmin(admin.ModelAdmin):
    list_display = ('movie_title', 'length', 'age_restriction')
    search_fields = ('movie_title', 'length', 'age_restriction')


admin.site.register(Movie, MovieAdmin)


class CinemaAdmin(admin.ModelAdmin):
    list_display = ('cinema_title', 'location')
    search_fields = ('cinema_title', 'location')


admin.site.register(Cinema, CinemaAdmin)
