from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Planet
from .serializers import PlanetSerializer

class PlanetListCreateAPIView(APIView):
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
      return Response(serializer.data, status=201)
    
    return Response(serializer.errors, status=422)
  
class PlanetRetrieveUpdateDestroyAPIView(APIView):
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
