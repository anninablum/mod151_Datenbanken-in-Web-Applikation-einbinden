from django import forms
from cinema.models import Cinema, Movie, TicketRegistraion, Customer


class CinemaForm(forms.ModelForm):
    class Meta:
        model = Cinema
        fields = ['cinema_title', 'location']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['movie'].queryset = Movie.objects.none()


class CustomerCreationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['title', 'first_name', 'last_name']
