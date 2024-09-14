# chief_wolf
# 9/12/2024
# See LICENSE in root directory for license information

from typing import *

class CelestialObject:
    def __init__( self, designation:str, magnitude:float, max_dimension:float, right_ascension:float, declination:float, common_name:str, object_type:str ):
        self.designation:str = designation
        self.magnitude:float = magnitude
        self.max_dimension:float = max_dimension
        self.right_ascension:float = right_ascension
        self.declination:float = declination
        
        self.common_name:str = common_name
        self.object_type:str = object_type
