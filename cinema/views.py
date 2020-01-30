from django.contrib.auth.decorators import login_required
from search_views.filters import BaseFilter
from django.contrib.auth import login
from django.db.models import query, Q
from abc import ABC
from django.views.generic import ListView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from search_views.views import SearchListView
from cinema.forms import CinemaForm, CustomerRegistrationForm, MovieSearchForm
from .models import Cinema, Movie, Customer


# Create your views here.

class MovieFilter(BaseFilter):
    search_fields = {
        'search_text': ['movie_title', 'genre'],
        'serch_age': {'operator': '__exact', 'fields': ['age_restriction']}
    }


class MovieSearchList(SearchListView):
    model = Movie
    paginate_by = 20
    template_name = "cinema/movie_list.html"
    form_class = MovieSearchForm
    filter_class = MovieFilter


# def cinema_from_db_view(request):
#     cinema_list = Cinema.objects.all()
#     return render(request, 'cinema/cinema_list.html', cinema_list)
#

@login_required
def customer_registration_view(request):
    cinema_list = Cinema.objects.all()
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'cinema/cinema_list.html', {'cinema': cinema_list})
    else:
        form = CustomerRegistrationForm()
    return render(request, 'cinema/registraion_customer.html', {'form': form})


##
# def customer_registration_view(request, id=0):
#     if request.method == "GET":
#         if id == 0:
#             form = CustomerRegistrationForm()
#         else:
#             customer = Customer.objects.get(pk=id)
#             form = CustomerRegistrationForm(instance=customer)
#         return render(request, "cinema/registraion_customer.html", {'form': form})
#     else:
#         if id == 0:
#             form = CustomerRegistrationForm(request.POST)
#         else:
#             customer = Customer.objects.get(pk=id)
#             form = CustomerRegistrationForm(request.POST, instance=customer)
#         if form.is_valid():
#             form.save()
#         return redirect('/cinema/movies/')


def customer_delete_view(request, id):
    customer = Customer.objects.get(pk=id)
    customer.delete()
    return redirect('/cinema/movies')


def cinema_movie_view(request):
    movie_list = Movie.objects.all()
    return render(request, 'cinema/movie_list.html', {'movie': movie_list})

# def ticket_registration_view(request):
#     ticket_list = Movie.objects.all()
#     if request.method == 'POST':
#         form = TicketRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'cinema/ticket_registration.html', {'tickets': ticket_list})
#     else:
#         form = CustomerRegistrationForm()
#     return render(request, 'cinema/ticket_registration.html', {'tickets': ticket_list})

# def cinema_movie_view(ListView):
#     model = Movie
#     template_name = 'search_results.html'

# class SearchResultsView(ListView):
#     model = Movie
#     template_name = 'cinema/movie_list.html'
#
#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         object_list = Movie.objects.filter(Q(name__icontains=query) | Q(state__icontains=query))
#         return object_list
