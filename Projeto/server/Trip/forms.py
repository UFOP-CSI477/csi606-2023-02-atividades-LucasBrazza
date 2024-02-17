from django import forms
from django.forms import ModelForm, ValidationError
from .models import Trip
import datetime


class TripForm(ModelForm):
    
    day = forms.DateField(widget=forms.SelectDateWidget)
    schedule = forms.TimeField(widget=forms.TimeInput)
    
    class Meta:
        model = Trip
        fields = [
            'origen',
            'destination',
            'day',
            'schedule',
            'driver',
            'vehicle',
            'vacancies',
            'seats_taken'
        ]
        
        def __init__(self):
            pass
        
        def clean_day(self):
            day = self.cleaned_data['day']
            if day < datetime.date.today():
                raise ValidationError('Day must be in the future')
            return day
        
        def clean_schedule(self):
            schedule = self.cleaned_data['schedule']
            if schedule < datetime.time.now():
                raise ValidationError('Schedule must be in the future')
            return schedule
        
        def clean_seats_taken(self):
            seats_taken = self.cleaned_data['seats_taken']
            if seats_taken < 0:
                raise ValidationError('Seats taken must be a positive number')
            return seats_taken