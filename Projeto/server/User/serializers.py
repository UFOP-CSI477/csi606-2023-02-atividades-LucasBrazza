from rest_framework import serializers
from .models import UserDriverModel, UserClientModel

class UserDriverSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    
    class Meta:
        model = UserDriverModel
        fields = [
            'id', 
            'name', 
            'cpf', 
            'email', 
            'password', 
            'password2',
            'phone', 
            'driver_license', 
            'vehicles_list'
        ]
        extra_kwargs = {
            'password': {'write_only': True}, 
        }
            
        def create(self, validated_data):
            validated_data['user_type'] = 'driver'
            return super().create(validated_data)

class UserClientSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    
    class Meta:
        model = UserClientModel
        fields = [
            'id', 
            'name', 
            'cpf', 
            'email', 
            'password', 
            'password2',
            'phone', 
        ]
        extra_kwargs = {
            'password': {'write_only': True}, 
        }
        
        def create(self, validated_data):
            validated_data['user_type'] = 'client'
            return super().create(validated_data)