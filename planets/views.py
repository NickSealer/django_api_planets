from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from .models import Planet
from .serializers import PlanetSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

class PlanetViewSet(ModelViewSet):
  queryset = Planet.objects.all()
  serializer_class = PlanetSerializer
  filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
  filterset_fields = [field.name for field in Planet._meta.fields if field.name != 'atmosphere']
  search_fields = ['name', 'planet_type', 'discovered_by']
  ordering_fields = ['name', 'planet_type', 'discovered_date', 'created_at']
  
  authentication_classes = [JWTAuthentication]
  # permission_classes = [AllowAny] # Default config
  
  def get_permissions(self):
    if self.action in ['list', 'retrieve']:
      return [AllowAny()]
    return [IsAuthenticated()]

