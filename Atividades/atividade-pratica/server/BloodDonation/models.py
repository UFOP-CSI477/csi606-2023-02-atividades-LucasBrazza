from django.db import models
from Person.models import Person
from BloodCenter.models import BloodCenter

class BloodDonation(models.Model):
    personId = models.ForeignKey(Person, on_delete=models.CASCADE)
    bloodCenterId = models.ForeignKey(BloodCenter, on_delete=models.CASCADE)
    date = models.DateField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)   