from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
    return render(request, "home/index.html", {})

def agency_list(request):
    agency_list = models.Agency.objects.all()
    return render(request, "home/agency-list.html", {"agency_list": agency_list})
