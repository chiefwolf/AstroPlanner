# chief_wolf
# 9/12/2024
# See LICENSE in root directory for license information

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
