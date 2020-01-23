<<<<<<< Updated upstream
# from django import forms
# from cinema.models import Cinema, Movie


# class CinemaForm(forms.ModelForm):
#     class Meta:
#         model = Cinema
#         fields = ['cinema_title', 'location']
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['movie'].queryset = Movie.objects.none()
=======
from django import forms
from cinema.models import Cinema, Movie


class CinemaForm(forms.ModelForm):
    class Meta:
        model = Cinema
        fields = ['cinema_title', 'location']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['movie'].queryset = Movie.objects.none()
>>>>>>> Stashed changes
