from django.urls import path
from . import views

app_name = 'cinema'

urlpatterns = [
    # path('', views.cinema_view, name='cinema'),
    # path('', views.cinema_from_db_view, name='cinemadb'),
    path('customer_registration/', views.customer_registration_view, name='customer'),
    path('customer_registration/<int:id>/', views.customer_registration_view, name='customer_update'),
    path('customer_registration/delete/<int:id>', views.customer_registration_view, name='customer_delete'),
    # path('movies/', views.cinema_movie_view, name='movie'),
    # path('tickets/', views.ticket_registration_view, name='tickets'),
]
