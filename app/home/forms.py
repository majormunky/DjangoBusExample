from django import forms
from . import models


class AgencyForm(forms.ModelForm):
    class Meta:
        model = models.Agency
        fields = ["name"]


class BusForm(forms.ModelForm):
    class Meta:
        model = models.Bus
        fields = ["name", "agency", "seat_configuration", "row_count"]


class BusTripForm(forms.ModelForm):
    class Meta:
        model = models.BusTrip
        fields = ["departure_time"]
