from django.contrib.auth import authenticate, login,  logout
from django.shortcuts import redirect
from django.views.generic import View
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import UserModel
from .serializers import UserDriverSerializer, UserClientSerializer
from User.permissions import IsOwnerOrSysManager, IsClientOrDriver, IsDriverOrSysManager, IsNotAuthenticated


class CreateDriverUserView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserDriverSerializer
    permission_classes = [IsNotAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateClientUserView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserClientSerializer
    permission_classes = [IsNotAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UpdateDriverUserView(generics.UpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserDriverSerializer
    permission_classes = [IsOwnerOrSysManager]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateClientUserView(generics.UpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserClientSerializer
    permission_classes = [IsOwnerOrSysManager]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DeleteUserView(generics.DestroyAPIView):
    queryset = UserModel.objects.all()
    permission_classes = [IsOwnerOrSysManager]
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class LoginView(View):
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirecione para a página inicial após o login
        else:
            return redirect('create_user')  # Redirecione para a página de criação de usuário se o login falhar
        
        
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')  # Redirecione para a página de login após o logout