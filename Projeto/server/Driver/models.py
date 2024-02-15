from django.db import models



class Driver(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, required=True)
    email = models.EmailField(max_length=100, unique=True, required=True)
    password = models.CharField(max_length=100, required=True)
    cpf = models.CharField(max_length=11, unique=True, required=True)
    phone = models.CharField(max_length=15, required=True)
    driver_license = models.IntegerField(max_length=12, unique=True, required=True)
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
    review = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f'{self.name} - {self.email}'
    
    