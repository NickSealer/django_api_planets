from django.urls import path
from .views import *

urlpatterns = [
  path('planets/', PlanetListCreateAPIView.as_view(), name='planet-list-create'),
  path('planets/<int:pk>/', PlanetRetrieveUpdateDestroyAPIView.as_view(), name='planet-detail'),
  path('planets/<int:pk>/assign_mission', AssignSpacialMission.as_view(), name='assign_spacil_mission'),
  path('planets/terraform_simulation', TerraformSimulation.as_view(), name='terraform_simulation'),
  path('planets/basic_info', BasicInfoWithFilters.as_view(), name='basic-info'),
  path('planets/<int:pk>/is_habitable', IsHabitable.as_view(), name='is_habitable'),
]