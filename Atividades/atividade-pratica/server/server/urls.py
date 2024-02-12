"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from State import views as state_views
from City import views as city_views
from Person import views as person_views
from BloodType import views as bloodtype_views
from BloodCenter import views as bloodcenter_views
from BloodDonation import views as blooddonation_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('states/', state_views.StatesList.as_view()),
    path('states/<int:id>', state_views.StateDetails.as_view()),
    path('cities/', city_views.CitiesList.as_view()),
    path('cities/<int:id>', city_views.CityDetails.as_view()),
    path('person/', person_views.PersonsList.as_view()),
    path('person/<int:id>', person_views.PersonDetails.as_view()),
    path('bloodtypes/', bloodtype_views.BlodTypesList.as_view()),
    path('bloodtypes/<int:id>', bloodtype_views.BloodTypeDetails.as_view()),
    path('bloodcenters/', bloodcenter_views.BloodCentersList.as_view()),
    path('bloodcenters/<int:id>', bloodcenter_views.BloodCenterDetails.as_view()),
    path('blooddonations/', blooddonation_views.BloodDonationsList.as_view()),
    path('blooddonations/<int:id>', blooddonation_views.BloodDonationDetails.as_view()),
    path('', bloodcenter_views.base_view)
]
