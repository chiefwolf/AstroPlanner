# chief_wolf
# 9/12/2024
# Copyright 2024 chief_wolf <camodude98@gmail.com>

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

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
