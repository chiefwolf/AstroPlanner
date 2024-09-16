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

from enum import Enum

class SphericalCoordinateSystems(Enum):
    ElAz = 0 # Local
    Equatorial = 1 
    Ecliptic = 2 # 
    Galactic = 3 # Sun-centered
