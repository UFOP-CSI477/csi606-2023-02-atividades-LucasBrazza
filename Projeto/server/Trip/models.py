from django.db import models
from Vehicles.models import Vehicle


class Trip(models.Model):
    id = models.AutoField(primary_key=True)
    origen = models.CharField(max_length=100, required=True)
    destination = models.CharField(max_length=100, required=True)
    day = models.DateField(required=True)
    schedule = models.TimeField(required=True)
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE)
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
    vacancies = models.IntegerField(default=Vehicle.seats_quantity)
    seats_taken = models.IntegerField(default=0)
    