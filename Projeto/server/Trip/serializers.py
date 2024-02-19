from rest_framework import serializers
from .models import TripModel, PassengerTripModel
from Vehicles.models import VehicleModel
from rest_framework.serializers import ModelSerializer


class PassengerTripSerializer(ModelSerializer):
    class Meta:
        model = PassengerTripModel
        fields = ['id', 'trip', 'passenger']
        
class TripSerializer(ModelSerializer):
    passengers = PassengerTripSerializer(many=True, read_only=True)
    
    class Meta:
        model = TripModel
        fields = [
            'id',
            'origen',
            'destination',
            'day',
            'scheduled_time',
            'driver',
            'vehicle',
            'vacancies',
            'seats_taken',
            'price',
            'passengers'
        ]
        
        def create(self, validated_data):
            if self.context["request"].user.user_type != "driver": 
                raise serializers.ValidationError("Apenas motoristas podem criar viagens.")
            validated_data["driver"] = self.context["request"].user
            validated_data["seats_taken"] = VehicleModel.objects.get(id=validated_data["vehicle"]).seats - validated_data["vacancies"]
            return TripModel.objects.create(**validated_data)

        def get_seats_taken(self, obj):
            return obj.vehicle.seats_quantity - obj.vacancies
        

class SearchTripSerializer(ModelSerializer):
    class Meta:
        model = TripModel
        fields = [
            'id',
            'origen',
            'destination',
            'day',
            'driver',
            'vehicle',
            'vacancies',
            'price',
            'passengers'
        ]  
        
        


        
   