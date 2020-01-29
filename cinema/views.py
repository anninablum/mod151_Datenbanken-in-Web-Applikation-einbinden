from django.contrib.auth import login
from django.shortcuts import render, redirect
from cinema.forms import CinemaForm, CustomerRegistrationForm
from .models import Cinema, Movie, Customer


# Create your views here.

# def cinema_from_db_view(request):
#     cinema_list = Cinema.objects.all()
#     return render(request, 'cinema/cinema_list.html', cinema_list)
#

# def customer_registration_view(request):
#     cinema_list = Cinema.objects.all()
#     if request.method == 'POST':
#         form = CustomerRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'cinema/registraion_customer.html', {'cinema': cinema_list})
#     else:
#         form = CustomerRegistrationForm()
#     return render(request, 'cinema/registraion_customer.html', {'form': form})

def customer_registration_view(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = CustomerRegistrationForm()
        else:
            customer = Customer.objects.get(pk=id)
            form = CustomerRegistrationForm(instance=customer)
        return render(request, "cinema/registraion_customer.html", {'form': form})
    else:
        if id == 0:
            form = CustomerRegistrationForm(request.POST)
        else:
            customer = Customer.objects.get(pk=id)
            form = CustomerRegistrationForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
        return redirect('/cinema/movies/')


def customer_delete_view(request, id):
    customer = Customer.objects.get(pk=id)
    customer.delete()
    return redirect('/cinema/movies')

# def cinema_movie_view(request):
#     movie_list = Movie.objects.all()
#     return render(request, 'cinema/movie_list.html', {'movie': movie_list})


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
