from django.forms import ModelForm, ValidationError
from .models import Driver

class DriverForm(ModelForm):
    class Meta:
        model = Driver
        fields = [
            'name',
            'email',
            'password',
            'cpf',
            'phone',
            'driver_license',
            'vehicle'
        ]
        
        def __init__(self):
            pass
        
        def clean_driver_license(self):
            driver_license = self.cleaned_data['driver_license']
            if len(driver_license) < 12:
                raise ValidationError('Driver license must be 12 digits')
            return driver_license
        