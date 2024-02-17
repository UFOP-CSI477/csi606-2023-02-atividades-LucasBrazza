from django.db import models
from User.models import UserModel

class Vehicle(models.Model):
    ENUM_VECHICLE_TYPE = (
        ('car', 'Car'),
        ('van', 'Van'),
        ('bus', 'Bus'),
    )
    
    id = models.AutoField(primary_key=True)
    plate = models.CharField(max_length=7, unique=True, blank=False)
    type =  models.CharField(max_length=30, choices=ENUM_VECHICLE_TYPE, blank=False)
    seats_quantity = models.IntegerField(blank=False)
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='vehicles', default=00000000000)

    def __str__(self):
        return f'{self.plate}'