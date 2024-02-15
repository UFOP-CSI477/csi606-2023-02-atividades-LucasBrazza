from django.db import models
from django.contrib.auth.models import AbstractUser

class UserType(models.TextChoices):
    CLIENT = 'client', 'Client'
    DRIVER = 'driver', 'Driver'
    SYS_MANAGER = 'sys_manager', 'Manager'

class UserClientModel(AbstractUser):
    CPF_REGEX = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    
    name = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=14, null=False, blank=False, unique=True, help_text='CPF must be in the format xxx.xxx.xxx-xx')
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)
    type = models.CharField(max_length=10, choices=UserType.choices, null=False, blank=False)


class UserDriverModel(AbstractUser):
    CPF_REGEX = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    
    name = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=14, null=False, blank=False, unique=True, help_text='CPF must be in the format xxx.xxx.xxx-xx')
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)
    type = models.CharField(max_length=10, choices=UserType.choices, null=False, blank=False)
    driver_license = models.CharField(max_length=20, blank=True, null=True)
    vehicles_list = models.JSONField(blank=True, null=True)