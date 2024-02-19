from django.urls import path
from .views import (
    TripCreateView, FinishedTripView, SearchTripView, DriverTripListView, PassengerTripListView, BookTripView, DeleteTripView
)

urlpatterns = [
    path('create/', TripCreateView.as_view(), name='create-trip'),
    
    path('delete/<int:trip>/', DeleteTripView.as_view(), name='delete-trip'),
    path('delete/', DeleteTripView.as_view(), name='delete-trip'),
    
    path('search/', SearchTripView.as_view(), name='search-trip'),
    path('search/?<str:origen>&<str:destination>&<str:day>', SearchTripView.as_view(), name='search-trip'),

    path('driver/', DriverTripListView.as_view(), name='list-driver-trip'),    
    path('driver/<int:driver>', DriverTripListView.as_view(), name='list-driver-trip'),
    
    path('passenger/', PassengerTripListView.as_view(), name='list-passenger-trip'),
    path('passenger/<int:passenger>', PassengerTripListView.as_view(), name='list-passenger-trip'),
    
    path('book/', BookTripView.as_view(), name='book-trip'),

]
