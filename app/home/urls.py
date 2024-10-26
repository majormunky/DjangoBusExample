from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("agencies/", views.agency_list, name="agency-list"),
    path("agencies/add/", views.add_agency, name="add-agency"),
    path("busses/", views.bus_list, name="bus-list"),
    path("busses/add/", views.add_bus, name="add-bus"),
    path("busses/<int:pk>/", views.bus_detail, name="bus-detail"),
    path("busses/<int:bus_pk>/add-trip/", views.add_bus_trip, name="add-bus-trip"),
    path("trip/<int:pk>/", views.bus_trip_detail, name="bus-trip-detail"),
]
