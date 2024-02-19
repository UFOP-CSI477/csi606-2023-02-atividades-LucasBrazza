from django.contrib.auth import login,  logout, authenticate
from django.shortcuts import redirect, render

from django.views.generic import View
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, GenericAPIView, RetrieveAPIView,RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserModel
from .serializers import UserDriverSerializer, UserPassengerSerializer, LoginSerializer
from User.permissions import IsOwnerOrSysManager, IsNotAuthenticated
from django.views import generic

class CreateDriverUserView(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserDriverSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreatePassengerUserView(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserPassengerSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UpdateDriverUserView(UpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserDriverSerializer
    # permission_classes = [IsOwnerOrSysManager]

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdatePassengerUserView(RetrieveUpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserPassengerSerializer
    # permission_classes = [IsOwnerOrSysManager]

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        print('instance', instance)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
class DeleteUserView(DestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserDriverSerializer
    # permission_classes = [IsOwnerOrSysManager]
    
    def destroy(self, request, *args, **kwargs):
        instance = request.query_params.get('trip', None)
        u = UserModel.objects.filter(pk=instance)
        self.perform_destroy(u)
        return Response({"success": "Motorista excluído com sucesso"}, status=status.HTTP_204_NO_CONTENT)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer
        print('serializer', serializer)
        validated_data = serializer.validate(self=serializer, data=request.data)

        if validated_data is not None:
            login(request, validated_data)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            # Verifique se o usuário existe e se as credenciais estão corretas
            try:
                UserModel.objects.get(username=serializer.validated_data['username'])
            except UserModel.DoesNotExist:
                return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'error': 'Senha incorreta'}, status=status.HTTP_401_UNAUTHORIZED)

              
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')  # Redirecione para a página de login após o logout
    
    
class HomeView(generic.TemplateView):
    template_name = 'index.html'