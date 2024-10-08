# chief_wolf
# 9/14/2024
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
import json

from src.IConfigurable import IConfigurable
from src.utils.DirectoryHelper import DirectoryHelper
from src.Logger import Logger

class ConfigHandler:
    def __init__( self, dir_helper:DirectoryHelper, logger:Logger, config_location:Union[str, bytes, os.PathLike] = "${configs}/default.json" ):
        self.dir_helper = dir_helper
        self.config_location:os.PathLike = self.dir_helper.replace_alias_strings(config_location) # Where does the config actually exist?
        self.config:Dict = {}
        self.configurables:Dict[ str, IConfigurable ] = {}
        self.logger:Logger = logger
    
    def register_configurable( self, configurable:IConfigurable ):
        if( ( configurable.json_section_name not in self.config ) and ( configurable.json_section_name not in self.configurables ) ):
            # Again, shouldn't need the second check but it's probably a good idea
            self.configurables[configurable.json_section_name] = configurable
            self.config[ configurable.json_section_name ] = configurable.default_vals
        else:
            self.logger.error( f'Value {configurable.json_section_name} already in confg {self.config_location}', 2 )
    
    def read_config( self ):
        config:Dict = json.load( self.config_location )

        self.logger.log( "Reading from the config file and building the universe from it..." )

        for key in config:
            # Do a quick check to see if this is a valid key
            if( ( key not in self.config ) or ( key not in self.configurables ) ):
                self.logger.delayed_warning( f'Value {key} in {self.config_location} not a valid key' )
                continue

            # Okay, it's a valid key, now actually do something about it
            self.configurables[key].register_values( config[key] )
        
        self.logger.execute_delayed_warning()

    def write_config( self ):
        with open( self.config_location, mode='at+' ) as file:
            json.dump( self.config, file, indent=4 )
