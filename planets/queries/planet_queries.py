from planets.models import Planet

class PlanetQueries():
  @classmethod
  def planets(cls):
    return Planet.objects.all()
  
  @classmethod
  def cold_basic_info(cls):
    planets_info = cls.planets().filter(
      has_life=False,temperature__lte=10,name__contains='xample'
    ).values('id', 'name', 'has_life', 'temperature', 'gravity', 'planet_type')
    return planets_info
  
  @classmethod
  def is_habitable(cls, pk: int) -> dict:
    try:
      planet = cls.planets().filter(
        pk=pk,
        temperature__lte=-50,
        planet_type='terrestrial',
        atmosphere__H2O__gt=50,
        atmosphere__O2__gt=10
      ).first()
      
      result = {
        'habitable': True if planet else False,
        'planet': planet.name if planet else None
      }

      return result
    except Planet.DoesNotExist as error:
      return f"Planet {pk} not found! Error: {error}"
  
  