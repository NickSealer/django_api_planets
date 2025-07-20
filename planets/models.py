from django.db import models

class Planet(models.Model):
  PLANET_TYPES = [
    ('terrestrial', 'Terrestre (rocoso)'),
    ('gas_giant', 'Gigante gaseoso'),
    ('ice_giant', 'Gigante helado'),
    ('dwarf', 'Planeta enano'),
    ('exoplanet', 'Exoplaneta'),
    ('super_earth', 'Súper Tierra'),
    ('hot_jupiter', 'Júpiter caliente'),
    ('lava_planet', 'Planeta de lava'),
    ('ocean', 'Planeta oceánico'),
    ('rogue', 'Planeta errante'),
    ('unknown', 'Desconocido'),
]
  
  name = models.CharField(max_length=100, null=False)
  mass = models.FloatField(help_text='In KM')
  radius = models.FloatField(help_text='In KM')
  orbital_period = models.FloatField(help_text='In day units')
  rotation_period = models.FloatField(help_text='In day units')
  distance_from_star = models.FloatField(help_text='KM')
  atmosphere = models.JSONField(default=dict)
  gravity = models.FloatField(help_text='Based in Earth gravity')
  has_life = models.BooleanField(default=False)
  temperature = models.CharField(help_text='In °C')
  planet_type = models.CharField(max_length=50, choices=PLANET_TYPES, default='unknown')
  discovered_by = models.CharField(max_length=100, null=False)
  discovered_date = models.DateField(null= False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"name: {self.name}, planet_type: {self.get_planet_type_display()}"  
  
