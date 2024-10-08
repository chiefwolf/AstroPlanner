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
import os
import datetime
from typing import Dict

from src.UniverseBuilder.UniverseBuilder import UniverseBuilder
from src.UniverseBuilder.CelestialObject import CelestialObject
from src.CoordinateSystem.SphericalCoordinateSystems import SphericalCoordinateSystems as scs
from src.Logger import Logger
from src.utils.angle_conversions import degree_minute_second_to_float, hour_minute_second_to_float
from src.IConfigurable import IConfigurable
from src.utils.DirectoryHelper import DirectoryHelper

class MessierBuilder( UniverseBuilder, IConfigurable ):
    def __init__( self, logger:Logger, dir_helper:DirectoryHelper, catalog_location: Union[ str, bytes, os.PathLike ]="${catalogs}/simple_messier_list.txt", max_processes:int = 1, use_messier:bool = True ):
        super().__init__( catalog_location, logger, max_processes )
        self.json_section_name = "messier_builder"
        self.default_vals = { "catalog_location":catalog_location, "num_processes":max_processes, "use_messier":use_messier }
        self.log = logger
        self.dir_helper:DirectoryHelper = dir_helper
        self.use_messier:bool = use_messier

    def get_objects(self, min_magnitude: float = 9) -> List[ CelestialObject ]:

        self.logger.log( 'Speaking Messier Objects into existance...' )
        time_start = datetime.datetime.now()
        
        objects:List[ CelestialObject ] = []
        
        # Single threaded, but it really doesn't to be multi-threaded because of how few Messier Objects there are
        with open( self.catalog_location, mode='r' ) as catalog:
            for line in  catalog :
                vals = line.split( ',' )

                if( vals[0][0] == '#' ):
                    # Pound is a comment line, skip it
                    continue
                
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

    def register_values(self, vals: Dict) -> None:
        super().register_values(vals)

        for key in vals:
            if( key == "catalog_location" ):
                self.catalog_location = self.dir_helper.replace_alias_strings( vals[key] )
            if( key == "num_processes" ):
                self.max_processes = int( vals[key] )
            if( key == "use_messier" ):
                self.use_messier = bool( vals[key] )
                
        return
    
    def update_catalog_location( self, loc:str ):
        self.catalog_location = loc
        self.default_vals['catalog_location'] = self.dir_helper.replace_dir_strings( loc )

        return
