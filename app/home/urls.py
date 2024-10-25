from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("agencies/", views.agency_list, name="agency-list"),
    path("agencies/add/", views.add_agency, name="add-agency"),
    path("busses/", views.bus_list, name="bus-list"),
]
