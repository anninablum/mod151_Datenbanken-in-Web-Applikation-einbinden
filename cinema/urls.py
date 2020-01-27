from django.urls import path
from . import views

app_name = 'cinema'

urlpatterns = [
    # path('', views.cinema_view, name='cinema'),
    path('', views.cinema_from_db_view, name='cinemadb'),
    path('customer_registration/', views.customer_registration_view, name='customer'),
]
