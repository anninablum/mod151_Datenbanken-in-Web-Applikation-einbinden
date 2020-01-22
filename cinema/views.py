from django.shortcuts import render
from .models import Cinema


# Create your views here.

def cinema_view(request):
    return render(request, 'cinema.html', {})


def cinema_from_db(request):
    cinema_list = Cinema.objects.all()
    return render(request, 'cinema.html', {'cinema': cinema_list})
