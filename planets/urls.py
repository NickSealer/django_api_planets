from django.urls import path
from .views import PlanetListCreateAPIView, PlanetRetrieveUpdateDestroyAPIView

urlpatterns = [
  path('planets/', PlanetListCreateAPIView.as_view(), name='planet-list-create'),
  path('planets/<int:pk>/', PlanetRetrieveUpdateDestroyAPIView.as_view(), name='planet-detail')
]