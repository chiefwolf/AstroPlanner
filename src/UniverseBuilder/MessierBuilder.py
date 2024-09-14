# chief_wolf
# 9/12/2024
# See LICENSE in root directory for license information

from typing import *
import os
import datetime

from src.UniverseBuilder.UniverseBuilder import UniverseBuilder
from src.UniverseBuilder.CelestialObject import CelestialObject
from src.CoordinateSystem.SphericalCoordinateSystems import SphericalCoordinateSystems as scs
from src.Logger import Logger
from src.utils.angle_conversions import degree_minute_second_to_float, hour_minute_second_to_float

class MessierBuilder( UniverseBuilder ):
    def __init__( self, catalog_location: Union[ str, bytes, os.PathLike ], logger:Logger, max_processes:int = 1 ):
        super().__init__( catalog_location, logger, max_processes )

    def get_objects(self, min_magnitude: float = 9) -> List[ CelestialObject ]:

        self.logger.log( 'Speaking Messier Objects into existance...' )
        time_start = datetime.datetime.now()
        
        objects:List[ CelestialObject ] = []
        
        with open( self.catalog_location, mode='r' ) as catalog:
            for idx, line in enumerate( catalog ):
                if not( idx == 0 ): # Skip the first line which explains the format...
                    vals = line.split( ',' )
                    
                    if( ( len(vals) > 1 ) and ( float(vals[1]) <= min_magnitude ) ):
                        # Need to convert from the format in the files to an actually usable format...
                        # val[0] is already a string, val[1] is easily transferred to a float

                        # val[2] is in the format degrees - minutes - seconds...
                        max_dim = degree_minute_second_to_float( vals[2] )
                        right_ascension = hour_minute_second_to_float( vals[3] )
                        declination = degree_minute_second_to_float( vals[4] )

                        if( vals[5].lower() == 'n/a' ):
                            vals[5] = vals[0]

                        objects.append( CelestialObject( designation=str(vals[0]), magnitude=float(vals[1]), max_dimension=max_dim, right_ascension=right_ascension, declination=declination, common_name=vals[5], object_type=vals[6] ) )

        self.logger.log( f'Building Messier Objects took: {datetime.datetime.now() - time_start}' )

        return objects
