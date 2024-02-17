from django.db import models
from Vehicles.models import VehicleModel
from User.models import UserModel
from django.contrib.auth import get_user_model


class TripModel(models.Model):
    
    class Meta:
        verbose_name = 'Trip'
        
    id = models.AutoField(primary_key=True)
    origen = models.CharField(max_length=100, blank=False)
    destination = models.CharField(max_length=100, blank=False)
    day = models.DateField(blank=False)
    scheduled_time = models.TimeField(blank=False)
    driver = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='trips_driven')
    vehicle = models.ForeignKey(VehicleModel, on_delete=models.CASCADE)
    vacancies = models.IntegerField(default=0)
    seats_taken = models.IntegerField(default=0)
    passengers = models.ManyToManyField(UserModel, through='PassengerTripModel', blank=True, related_name='trips_taken')
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    
    def __str__(self):
        return f'{self.origen} - {self.destination} - {self.day} - {self.scheduled_time} - {self.driver}'


class PassengerTripModel(models.Model):
    
    class Meta:
        verbose_name = 'intermediate Trips-Passengers Table'
    
    id = models.AutoField(primary_key=True)
    trip = models.ForeignKey(TripModel, on_delete=models.CASCADE)
    passenger = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    