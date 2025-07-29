from planets.models import Planet

class AssignSpacialMissionService():
  def __init__(self, planet: Planet, request):
    self.planet = planet
    self.request = request
    
  def execute(self) -> dict:
    missions = self._available_missions()
    mission = self.request.data.get('mission')
    if mission == 'destruir':
      return {'success': False, 'message': f"current mission {mission} not authorized yet."}
      
    if mission in missions:
      return {'success': True, 'planet': self.planet.name, 'mission': mission, 'message': 'Mission Assigned.'}
    else:
      return {'success': False, 'message': 'Mission not found'}
    
  def _available_missions(self):
    if self.planet.planet_type == 'terrestrial':
      return ['colonizar', 'destruir', 'estudiar', 'expedicionar']
    else:
      return ['explorar']
    