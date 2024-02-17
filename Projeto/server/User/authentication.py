from rest_framework import authentication
from .models import UserModel

class CustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        user = UserModel.objects.get(username=request.data['username'])
        
        if user and user.password == request.data['password']:
            return (user, None)
        return None