from django.db import models
from enum import Enum

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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.plate}'