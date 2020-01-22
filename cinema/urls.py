from django.urls import path
from . import views


app_name = 'cinema'


urlpatterns = [
    path('', views.cinema_view, name='cinema'),
    path('from_db/', views.cinema_from_db, name='cinema'),
]
