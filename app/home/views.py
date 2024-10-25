from django.shortcuts import render, redirect
from . import models
from . import forms

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
            form.save()
            return redirect("bus-list")
    else:
        form = forms.BusForm()
    return render(request, "home/add-bus.html", {"form": form})
