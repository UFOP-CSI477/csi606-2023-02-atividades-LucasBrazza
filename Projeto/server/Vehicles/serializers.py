from rest_framework import serializers
from .models import VehicleModel

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = ['plate', 'type', 'seats_quantity', 'owner']

class VehicleSerializerDelete(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = []
        

class VehicleSerializerID(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = ['id', 'plate', 'type', 'seats_quantity', 'owner']

    def get(self, request, *args, **kwargs):
        
        return 