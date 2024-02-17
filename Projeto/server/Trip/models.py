from django.db import models
from Vehicles.models import Vehicle


class TripModel(models.Model):
    id = models.AutoField(primary_key=True)
    origen = models.CharField(max_length=100, blank=False)
    destination = models.CharField(max_length=100, blank=False)
    day = models.DateField(blank=False)
    scheduled_time = models.TimeField(blank=False)
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE)
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
    vacancies = models.IntegerField(default=Vehicle.seats_quantity)
    seats_taken = models.IntegerField(default=Vehicle.seats_quantity - vacancies)
    passengers = models.ManyToManyField('Passenger', null=True, blank=True, through='PassengerTripMode')
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    
    
class PassengerTripModel(models.Model):
    id = models.AutoField(primary_key=True)
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    passenger = models.ForeignKey('Passenger', on_delete=models.CASCADE)
    