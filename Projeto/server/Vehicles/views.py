from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from .models import Vehicle
from .serializers import VehicleCreateSerializer, VehicleSerializer
from User.permissions import IsOwnerOrSysManager, IsClientOrDriver, IsDriverOrSysManager, IsNotAuthenticated
from rest_framework.response import Response
from rest_framework import status



from .models import Vehicle

class UserVehiclesListView(ListAPIView):
    model = Vehicle
    serializer_class = VehicleSerializer
    permission_classes = [IsDriverOrSysManager]
    
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Vehicle.objects.filter(users__id=user_id)

class VehicleCreateView(CreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleCreateSerializer
    permission_classes = [IsDriverOrSysManager]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Verifica se o usuário tem permissão para criar um veículo
            if  request.user.type not in ['client', 'driver']:
                return Response({"error": "Você não tem permissão para criar um veículo."}, status=status.HTTP_403_FORBIDDEN)

            # Cria o veículo
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class VehicleDeleteView(DestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [IsOwnerOrSysManager]
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
