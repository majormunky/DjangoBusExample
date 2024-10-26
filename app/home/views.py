from django.shortcuts import render, redirect, get_object_or_404
from . import models
from . import forms
from . import utils

# Create your views here.
def index(request):
    return render(request, "home/index.html", {})

def agency_list(request):
    agency_list = models.Agency.objects.all()
    return render(request, "home/agency-list.html", {"agency_list": agency_list})

def add_agency(request):
    if request.method == "POST":
        form = forms.AgencyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("agency-list")
    else:
        form = forms.AgencyForm()
    return render(request, "home/add-agency.html", {"form": form})

def bus_list(request):
    bus_list = models.Bus.objects.all()
    return render(request, "home/bus-list.html", {"bus_list": bus_list})

def add_bus(request):
    if request.method == "POST":
        form = forms.BusForm(request.POST)
        if form.is_valid():
            item = form.save()
            utils.add_seats_for_bus(item)
            return redirect("bus-list")
    else:
        form = forms.BusForm()
    return render(request, "home/add-bus.html", {"form": form})

def bus_detail(request, pk):
    bus_data = get_object_or_404(models.Bus, pk=pk)
    seat_list = models.Seat.objects.filter(bus=bus_data).order_by("row", "column")
    seat_data = utils.organize_seats_for_bus(bus_data, seat_list)
    bus_trips = models.BusTrip.objects.filter(bus=bus_data).order_by("departure_time")
    return render(request, "home/bus-detail.html", {"bus_data": bus_data, "seat_data": seat_data, "bus_trips": bus_trips})

def add_bus_trip(request, bus_pk):
    bus_data = get_object_or_404(models.Bus, pk=bus_pk)
    if request.method == "POST":
        form = forms.BusTripForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.bus = bus_data
            item.save()
            return redirect("bus-detail", pk=bus_pk)
    else:
        form = forms.BusTripForm()
    return render(request, "home/add-bus-trip.html", {"form": form})
