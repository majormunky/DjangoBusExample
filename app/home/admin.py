from django.contrib import admin
from . import models

admin.site.register(models.Bus)
admin.site.register(models.Seat)
admin.site.register(models.BusTrip)
admin.site.register(models.SeatUserLink)
