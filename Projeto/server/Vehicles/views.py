from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.generics import ListAPIView

from .models import Vehicle

class VehicleList(ListView):
    model = Vehicle
    template_name = 'vehicle_list.html'
    context_object_name = 'vehicles'
    
    def get_queryset(self):
        return Vehicle.objects.all()
    
    
    