from django import forms
from cinema.models import Cinema, Customer, Movie
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CinemaForm(forms.ModelForm):
    class Meta:
        model = Cinema
        fields = ['cinema_title', 'location']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['movie'].queryset = Movie.objects.none()


class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['title', 'first_name', 'last_name', 'email', 'movie']

    # def __init__(self, *args, **kwargs):
    #     super(CustomerRegistrationForm, self).__init__(*args, **kwargs)
    #     self.fields['title'].empty_label = "Select"


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['movie_title', 'movie_genre', ]


class MovieSearchForm(forms.Form):
    search_text = forms.CharField(
        required=False,
        label='Search',
        widget=forms.TextInput(attrs={'placeholder': 'search here'})
    )
    search_age = forms.IntegerField(
        required=False,
        label= 'Search age restriction'
    )


# class TicketRegistrationForm(forms.ModelForm):
#     class Meta:
#         model = TicketRegistration
#         fields = ['fk_customer', 'fk_movie']
