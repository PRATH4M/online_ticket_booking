# booking/models.py
from django.db import models
from django.conf import settings

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    total_seats = models.IntegerField()

    def __str__(self):
        return self.name

    def available_seats(self):
        booked_seats = sum(booking.seats for booking in self.booking_set.all())
        return self.total_seats - booked_seats

class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Foreign key to user model
    user_name = models.CharField(max_length=200)
    seats = models.IntegerField()

    def __str__(self):
        return f"{self.user_name} - {self.event.name}"
