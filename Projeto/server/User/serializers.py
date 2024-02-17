from rest_framework import serializers
from .models import UserModel

class UserDriverSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)
    
    class Meta:
        model = UserModel
        fields = [
            'username',
            'name', 
            'last_name',
            'cpf', 
            'email', 
            'password', 
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
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)
    class Meta:
        model = UserModel
        fields = [
            'username',
            'name', 
            'last_name',
            'cpf', 
            'email', 
            'password', 
            'phone', 
        ]
        extra_kwargs = {
            'password': {'write_only': True}, 
        }
        
        def create(self, validated_data):
            validated_data['user_type'] = 'passenger'
            return super().create(validated_data)
        


from rest_framework import serializers
from django.contrib.auth import get_user_model


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    def validate(self, data):
        user = UserModel.objects.filter(username=data['username']).first()
        if user is None or user.password != data['password']:
            raise serializers.ValidationError({'error': 'Invalid credentials'})
        return user
    
