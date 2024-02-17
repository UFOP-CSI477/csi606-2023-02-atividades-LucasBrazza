from rest_framework import serializers
from .models import VehicleModel, VehicleType

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = ['plate', 'type', 'seats_quantity']


    def create(self, validated_data):
        
        validated_data['owner'] = self.context['request'].user

        # Definir seats_quantity automaticamente com base no tipo de veículo
        vehicle_type = validated_data['type']
        if vehicle_type == VehicleType.CAR.value:
            validated_data['seats_quantity'] = 4
        elif vehicle_type == VehicleType.BUS.value:
            validated_data['seats_quantity'] = 40
        elif vehicle_type == VehicleType.VAN.value:
            validated_data['seats_quantity'] = 12

        return super().create(validated_data)