from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from rest_framework import permissions, serializers, viewsets, status
from rest_framework.response import Response 
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, GenericAPIView
from Vehicles.models import VehicleModel
from .models import TripModel, PassengerTripModel
from .serializers import PassengerTripSerializer, TripSerializer, SearchTripSerializer
from User.permissions import IsDriverOrSysManager, IsPassengerOrDriver, IsNotAuthenticated

class TripCreateView(CreateAPIView):
    queryset = TripModel.objects.all()
    serializer_class = TripSerializer



class ListTripView(ListAPIView):
    queryset = TripModel.objects.all()
    serializer_class = TripSerializer
    

class SearchTripView(GenericAPIView):
    queryset = TripModel.objects.all()
    serializer_class = SearchTripSerializer

    def get(self, request, *args, **kwargs):
        origen = request.query_params.get('origen', None)
        destination = request.query_params.get('destination', None)
        day = request.query_params.get('day', None)
        queryset = origen + destination + day

        if queryset is not None:
            queryset = TripModel.objects.filter(day=day, origen__icontains=origen, destination__icontains=destination)
            print('queryset', queryset)
            return Response(self.get_serializer(queryset, many=True).data)
        return Response({"error": "Nenhuma viagem encontrada"}, status=status.HTTP_404_NOT_FOUND)
    
class FinishedTripView(DestroyAPIView):
    queryset = TripModel.objects.all()
    serializer_class = TripSerializer
    permission_classes = [IsDriverOrSysManager]
    
    

class PassengerTripListView(ListAPIView):
    queryset = TripModel.objects.all()
    serializer_class = SearchTripSerializer
    
    def get(self, request, *args, **kwargs):
        passenger = request.query_params.get('passenger', None)
        print('passenger', passenger)
        
        if passenger is not None:
            queryset = TripModel.objects.filter(passengers__cpf=passenger)
            print('queryset', queryset)
            return Response(self.get_serializer(queryset, many=True).data)

        return Response({"error": "Nenhuma viagem encontrada"}, status=status.HTTP_404_NOT_FOUND)
    

class DriverTripListView(ListAPIView):
    queryset = TripModel.objects.all()
    serializer_class = SearchTripSerializer
    
    def get(self, request, *args, **kwargs):
        driver = request.query_params.get('driver', None)
        print('driver', driver)
        
        if driver is not None:
            queryset = TripModel.objects.filter(driver__cpf=driver)
            print('queryset', queryset)
            return Response(self.get_serializer(queryset, many=True).data)

        return Response({"error": "Nenhuma viagem encontrada"}, status=status.HTTP_404_NOT_FOUND)
    
class BookTripView(CreateAPIView):
    serializer_class = PassengerTripSerializer
    # permission_classes = [IsPassengerOrDriver]
    
    def create(self, request, *args, **kwargs):
        # Obtém os dados da solicitação
        trip_id = request.data.get('trip')
        passenger = request.data.get('passenger')
        
        # Verifica se a viagem existe
        try:
            trip = TripModel.objects.get(pk=trip_id)
        except TripModel.DoesNotExist:
            return Response({"error": "Viagem não encontrada"}, status=status.HTTP_404_NOT_FOUND)
        
        # Verifica se há vagas disponíveis
        if trip.vacancies <= 0:
            return Response({"error": "Não há vagas disponíveis para esta viagem"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Verifica se o passageiro já está na viagem
        if trip.passengers.filter(cpf=passenger).exists():
            return Response({"error": "Você já está nesta viagem"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Cria a relação entre a viagem e o passageiro
        PassengerTripModel.objects.create(trip=trip, passenger_id=passenger)
        
        # Atualiza a quantidade de vagas disponíveis
        trip.vacancies -= 1
        trip.save()
        
        return Response({"success": "Viagem reservada com sucesso"}, status=status.HTTP_201_CREATED)
   

class DeleteTripView(DestroyAPIView):
    queryset = TripModel.objects.all()
    serializer_class = TripSerializer
    # permission_classes = [IsDriverOrSysManager]
    
    def destroy(self, request, *args, **kwargs):
        query = request.query_params.get('trip', None)
        instance = TripModel.objects.filter(id=query)
        self.perform_destroy(instance)
        return Response({"success": "Viagem excluída com sucesso"}, status=status.HTTP_204_NO_CONTENT)