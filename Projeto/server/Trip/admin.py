from django.contrib import admin
from .models import TripModel, PassengerTripModel

admin.site.register(TripModel)
admin.site.register(PassengerTripModel)
