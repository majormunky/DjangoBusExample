from django.db import models
from django.contrib.auth import get_user_model


class Agency(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Bus(models.Model):
    SEAT_CONFIG_CHOICES = (
        ("1x1", "1x1"),
        ("2x2", "2x2"),
        ("2x3", "2x3"),
    )
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    seat_configuration = models.CharField(max_length=10, choices=SEAT_CONFIG_CHOICES)
    row_count = models.IntegerField()

    def __str__(self):
        return self.name


class BusTrip(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()


class Seat(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    column = models.IntegerField()
    row = models.IntegerField()
    person = models.ManyToManyField(get_user_model(), through="SeatUserLink")

    def __str__(self):
        return f"R{self.row}-C{self.column}"


class SeatUserLink(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    departure_time = models.ForeignKey(BusTrip, on_delete=models.CASCADE)
