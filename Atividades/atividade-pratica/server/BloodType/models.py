from django.db import models

class BloodType(models.Model):
    type = models.CharField(max_length=2)
    factor = models.CharField(max_length=1)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def get_complete_blood_type(self):
        return self.type + self.factor
    
    def __str__(self):
        return self.type + self.factor