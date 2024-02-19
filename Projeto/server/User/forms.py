from django import forms
from .models import UserModel

class UserDriverForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    
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

class UserPassengerForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
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
        

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def validate(self, data):
        user = UserModel.objects.filter(username=data['username']).first()
        if user is None or user.password != data['password']:
            raise forms.ValidationError({'error': 'Invalid credentials'})
        return user
    
