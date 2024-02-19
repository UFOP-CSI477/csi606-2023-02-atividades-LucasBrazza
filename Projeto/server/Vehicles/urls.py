from django.contrib import admin
from django.urls import path
from Vehicles.views import VehicleCreateView, UserVehiclesListView, VehicleDeleteView

urlpatterns = [
    path('create/', VehicleCreateView.as_view(), name='create-vehicle'),
    path('list/?<int:owner>/', UserVehiclesListView.as_view(), name='list-vehicle'),
    path('list/', UserVehiclesListView.as_view(), name='list-vehicle'),
    path('delete/<int:vehicle_delete>/', VehicleDeleteView.as_view(), name='delete-vehicle'),
    path('delete/', VehicleDeleteView.as_view(), name='delete-vehicle'),
]