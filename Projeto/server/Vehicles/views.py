from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, GenericAPIView
from .models import VehicleModel
from .serializers import VehicleSerializer, VehicleSerializerDelete, VehicleSerializerID
from User.permissions import IsOwnerOrSysManager, IsDriverOrSysManager
from rest_framework.response import Response
from rest_framework import status



from .models import VehicleModel

from rest_framework.response import Response

class UserVehiclesListView(ListAPIView):
    model = VehicleModel
    serializer_class = VehicleSerializerID
    queryset = VehicleModel.objects.all()
    # permission_classes = [IsDriverOrSysManager]

    def get(self, request, *args, **kwargs):
        owner = request.query_params.get('owner', None)
        if owner is None:
            queryset = VehicleModel.objects.all()
        else :
            queryset = VehicleModel.objects.filter(owner=owner)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
    
class VehicleCreateView(CreateAPIView):
    queryset = VehicleModel.objects.all()
    serializer_class = VehicleSerializer
    # permission_classes = [IsDriverOrSysManager]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Cria o veículo
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class VehicleDeleteView(DestroyAPIView):
    queryset = VehicleModel.objects.all()
    serializer_class = VehicleSerializerDelete
    # permission_classes = [IsOwnerOrSysManager]
    
    def destroy(self, request, *args, **kwargs):
        instance = request.query_params.get('vehicle_delete', None)
        v = VehicleModel.objects.get(pk=instance)
        self.perform_destroy(v)
        return Response({"success": "Veículo excluído com sucesso"}, status=status.HTTP_204_NO_CONTENT)
    
    
