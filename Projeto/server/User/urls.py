from django.urls import path
from .views import (
    CreateDriverUserView, CreatePassengerUserView,
    UpdateDriverUserView, UpdatePassengerUserView,
    DeleteUserView
)

urlpatterns = [
    path('driver/create/', CreateDriverUserView.as_view(), name='singup-driver'),
    path('passenger/create/', CreatePassengerUserView.as_view(), name='singup-passenger'),
    path('driver/update/<int:driver_up>/', UpdateDriverUserView.as_view(), name='update-driver'),
    path('driver/update/', UpdateDriverUserView.as_view(), name='update-driver'),
    path('passenger/update/<int:pass_up>/', UpdatePassengerUserView.as_view(), name='update-passenger'),
    path('passenger/update/', UpdatePassengerUserView.as_view(), name='update-passenger'),
    path('delete/<int:driver_delete>/', DeleteUserView.as_view(), name='delete-user'),
    path('delete/', DeleteUserView.as_view(), name='delete-user'),
]