from django.contrib.auth import login
from django.shortcuts import render, redirect
from cinema.forms import CinemaForm, CustomerCreationForm
from .models import Cinema


# Create your views here.

# def cinema_view(request):
#     return render(request, 'cinema/cinema.html', {})


# def cinema_from_db(request):
#     cinema_list = Cinema.objects.all()
#     if request.method == "POST":
#         form = CinemaForm(request.POST)
#         if form.is_valid():
#             cinema = form.save(commit=False)
#             cinema.save()
#             return render(request, 'cinema/cinema.html', {})
#         else:
#             form = CinemaForm()
#         return render(request, 'cinema/cinema_dropdown.html', {'form': form})


def cinema_from_db_view(request):
    cinema_list = Cinema.objects.all()
    return render(request, 'cinema/cinema_dropdown.html', {'cinema': cinema_list})


def customer_registration_view(request):
    if request.method == 'POST':
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            form.auto_id()
            form.save()
            user = form.save()
            login(request, user)
            return redirect('cinema:cinema')
    else:
        form = CustomerCreationForm()
    return render(request, 'cinema/registraion_customer.html', {'form': form})
