from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import UserDriverModel, UserClientModel
from .serializers import UserDriverSerializer, UserClientSerializer
from . import permissions

class CreateDriverUserView(generics.CreateAPIView):
    queryset = UserDriverModel.objects.all()
    serializer_class = UserDriverSerializer
    permission_classes = [permissions.IsNotAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateClientUserView(generics.CreateAPIView):
    queryset = UserClientModel.objects.all()
    serializer_class = UserClientSerializer
    permission_classes = [permissions.IsNotAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UpdateDriverUserView(generics.UpdateAPIView):
    queryset = UserDriverModel.objects.all()
    serializer_class = UserDriverSerializer
    permission_classes = [permissions.IsOwnerOrSysManager]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateClientUserView(generics.UpdateAPIView):
    queryset = UserClientModel.objects.all()
    serializer_class = UserClientSerializer
    permission_classes = [permissions.IsOwnerOrSysManager]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
