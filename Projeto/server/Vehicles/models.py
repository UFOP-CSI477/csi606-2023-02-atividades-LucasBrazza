from django.db import models
from enum import Enum

class VehicleType(Enum):
    CAR = "CAR"
    BUS = "BUS"
    VAN = "Van"

class Vehicle(models.Model):
    
    ENUM_VECHICLE_TYPE = ()
    
    id = models.AutoField(primary_key=True)
    plate = models.CharField(max_length=7, unique=True, required=True)
    type =  models.CharField(max_length=30, choices=VehicleType, required=True)
    seats_quantity = models.IntegerField(required=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.type} - {self.plate}'