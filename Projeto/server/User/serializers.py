from rest_framework import serializers
from .models import UserModel

class UserDriverSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    
    class Meta:
        model = UserModel
        fields = [
            'id', 
            'name', 
            'cpf', 
            'email', 
            'password', 
            'password2',
            'phone', 
            'driver_license'
        ]
        extra_kwargs = {
            'password': {'write_only': True}, 
        }
            
        def create(self, validated_data):
            validated_data['user_type'] = 'driver'
            return super().create(validated_data)

class UserPassengerSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    
    class Meta:
        model = UserModel
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
            validated_data['user_type'] = 'passenger'
            return super().create(validated_data)