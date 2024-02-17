from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    
    USER_TYPES = (
        ('driver', 'Driver'),
        ('passenger', 'Passenger'),
        ('sys_manager', 'Manager')
    )
    
    first_name = None
    last_login = None
    user_permissions = None
    groups = None
    
    CPF_REGEX = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    
    password = models.CharField(max_length=128, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(primary_key=True, max_length=14, null=False, blank=False, unique=True, help_text='CPF must be in the format xxx.xxx.xxx-xx')
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)
    type = models.CharField(max_length=15, choices=USER_TYPES, null=False, blank=False)
    driver_license = models.CharField(max_length=20, blank=True, null=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    

