from django.shortcuts import render
from cinema.forms import CinemaForm
from .models import Cinema


# Create your views here.

def cinema_view(request):
    return render(request, 'cinema/cinema.html', {})


def cinema_from_db(request):
    # cinema_list = Cinema.objects.all()
    if request.method == "POST":
        form = CinemaForm(request.POST)
        if form.is_valid():
            cinema = form.save(commit=False)
            cinema.save()
        else:
            form = CinemaForm()
        return render(request, 'cinema/cinema_dropdown.html', {'cinema': form})
    return render(request, 'cinema.html', {})


# def cinema_from_db(request):
#     cinema_list = Cinema.objects.all()
#     return render(request, 'cinema_dropdown.html', {'cinema': cinema_list})


