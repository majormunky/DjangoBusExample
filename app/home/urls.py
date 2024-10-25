from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("agency-list/", views.agency_list, name="agency-list"),
]
