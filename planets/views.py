from decouple import config as env_config
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Planet
from .tasks import send_new_planet_email_task
from .serializers import PlanetSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated

class PlanetListCreateAPIView(APIView):
  authentication_classes = [JWTAuthentication]
  
  def get_permissions(self):
    if self.request.method == 'GET':
      return [AllowAny()]
    return [IsAuthenticated()]
  
  PLANET_FIELDS = [field.name for field in Planet._meta.fields]
  
  def get_planets(self, request) -> list[Planet]:
    field = request.query_params.get('field')
    value = request.query_params.get('value')
    
    if field in self.PLANET_FIELDS:
      return Planet.objects.filter(**{f"{field}__icontains": value})
    else:
      return Planet.objects.all()
      
  def get(self, request):
    planets = self.get_planets(request=request)
    serializer = PlanetSerializer(planets, many=True)
    return Response(serializer.data, status=200)
  
  def post(self, request):
    serializer = PlanetSerializer(data=request.data)
    
    if serializer.is_valid():
      serializer.save()
      
      data = {
        'subject': "New Planet Created",
        'to_emails': [request.user.email],
        'from_email': env_config('SMTP_USERNAME'),
        'template': 'emails/new_planet.html',
        'text_content': f"New planet {serializer.data.get('name')} creado por: {request.user.username}",
        'context': {'user': request.user.username, 'planet': serializer.data.get('name')}
      }
      
      send_new_planet_email_task.delay(data=data)
      
      return Response(serializer.data, status=201)
    
    return Response(serializer.errors, status=422)
  
class PlanetRetrieveUpdateDestroyAPIView(APIView):
  authentication_classes = [JWTAuthentication]
  
  def get_permissions(self):
    if self.request.method == 'GET':
      return [AllowAny()]
    return [JWTAuthentication()]
  
  def get(self, request, pk):
    planet = get_object_or_404(Planet, pk=pk)
    seriallizer = PlanetSerializer(planet)
    return Response(seriallizer.data, status=200)
  
  def put(self, request, pk):
    planet = get_object_or_404(Planet, pk=pk)
    serializer = PlanetSerializer(planet, data=request.data, partial=True)
    
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=200)
    
    return Response(serializer.errors, status=422)
  
  def delete(self, request, pk):
    planet = get_object_or_404(Planet, pk=pk)
    planet.delete()
    return Response({'message': f"Planet {pk} deleted."}, status=204)
