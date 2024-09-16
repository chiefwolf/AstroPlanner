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

from abc import ABC, abstractmethod
from typing import *
from src.UniverseBuilder.CelestialObject import CelestialObject
from src.Logger import Logger
import os

class UniverseBuilder(ABC):
    def __init__( self, catalog_location: Union[ str, bytes, os.PathLike ], logger:Logger, max_processes:int = 1 ):
        self.catalog_location: Union[ str, bytes, os.PathLike ] = catalog_location
        self.max_processes:int = max_processes
        self.logger = logger

    @abstractmethod
    def get_objects( self, min_magnitude:float = 9.0 ) -> List[ CelestialObject ]:
        ...
