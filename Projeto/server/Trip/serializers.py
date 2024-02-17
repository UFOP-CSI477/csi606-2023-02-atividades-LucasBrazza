from rest_framework import serializers
from .models import TripModel, PassengerTripMode
from Vehicles.models import Vehicle
from .models import PassengerTripModel

class PassengerTripModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassengerTripMode
        fields = ['trip', 'passenger']


class TripSerializer(serializers.ModelSerializer):
    passengers = PassengerTripModeSerializer(many=True, read_only=True)
    
    class Meta:
        model = TripModel
        fields = [
            'origen',
            'destination',
            'day',
            'scheduled_time',
            'vehicle',
            'vacancies',
            'seats_taken',
            'price',
        ]
        
        def create(self, validated_data):
            if self.context["request"].user.user_type != "driver": 
                raise serializers.ValidationError("Only drivers can create trips")
            validated_data["driver"] = self.context["request"].user
            validated_data["seats_taken"] = Vehicle.objects.get(id=validated_data["vehicle"]).seats - validated_data["vacancies"]
            trip = TripModel.objects.create(**validated_data)
            passengers = validated_data.pop('passengers')
            for passenger in passengers:
                PassengerTripMode.objects.create(trip=trip, passenger=passenger)
            return trip
        

class PassengerTripModelSerializer(ModelSerializer):
    class Meta:
        model = PassengerTripModel
        fields = ['trip', 'passenger']