from django.urls import path
from .views import (
    CreateDriverUserView, CreatePassengerUserView,
    UpdateDriverUserView, UpdatePassengerUserView,
    DeleteUserView
)

urlpatterns = [
    path('driver/create/', CreateDriverUserView.as_view(), name='singup-driver'),
    path('passenger/create/', CreatePassengerUserView.as_view(), name='singup-passenger'),
    path('driver/update/<int:pk>/', UpdateDriverUserView.as_view(), name='update_driver_user'),
    path('passenger/update/<int:pk>/', UpdatePassengerUserView.as_view(), name='update_passenger_user'),
    path('user/delete/<int:pk>/', DeleteUserView.as_view(), name='delete_user'),
]