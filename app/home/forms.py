from django import forms
from . import models


class AgencyForm(forms.ModelForm):
    class Meta:
        model = models.Agency
        fields = ["name"]
