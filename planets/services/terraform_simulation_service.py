from typing import Self
from functools import reduce

class TerraformSimulationService():
  def __init__(self, request):
    self.request = request
    self.ready = False
    self.probability = 0.00
    
  def execute(self) -> Self:
    atmosphere = self.request.data.get('atmosphere')
    
    if not atmosphere:
      return self
   
    total_atmosphere = reduce(lambda x, y: x+y, list(atmosphere.values()))
    
    if total_atmosphere > 100.00:
      self.probability = total_atmosphere * -1
      return self
    
    if atmosphere.get('H2O') and atmosphere.get('H2O') > 50.00:
      self.probability += 25.00
      
    if atmosphere.get('O2') and atmosphere.get('O2') > 25.50:
      self.probability += 30.00
      
    if self.probability >= 50.00:
      self.ready = True
      
    return self