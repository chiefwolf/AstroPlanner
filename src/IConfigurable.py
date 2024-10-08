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
from abc import ABC, abstractmethod

from src.Logger import Logger

class IConfigurable( ABC ):
    '''
    IConfigurable is meant to provide the interface to allow for elements that are to be controlled by some configuration file (mostly aimed at JSON)
    '''

    def __init__( self, json_section_name:str, default_vals:Dict, logger:Logger ):
        self.json_section_name:str = json_section_name
        self.default_vals:Dict = default_vals
        self.sub_configurables:Dict[str,IConfigurable] = {}
        self.log:Logger = logger
    
    def add_sub_configurable( self, configurable:'IConfigurable' ) -> None:
        '''
        add_sub_configurable will add another IConfigurable to its json_section_name (json_section_name={...})
        '''
        # Shouldn't need the second check but better safe than sorry....
        if( ( configurable.json_section_name in self.default_vals ) or ( configurable.json_section_name in self.sub_configurables ) ):
            raise KeyError( f"Value {configurable.json_section_name} is already assigned to a value in {self.json_section_name}" )

        # Register in both the values dictionary and in the sub-configuration dictionary for easy retrieval later
        self.default_vals[configurable.json_section_name] = configurable.default_vals
        self.sub_configurables[configurable.json_section_name] = configurable

    @abstractmethod
    def register_values( self, vals:Dict ) -> None:
        '''
        register_values takes the dictionary created from the configuration file and push it to the sub-classes. It is up to the child class to actually do something with the values.
        '''
        for key in vals:
            if( ( key not in self.default_vals ) or ( key not in self.sub_configurables ) ):
                self.log.delayed_warning( f"{key} in section {self.json_section_name} is not a known configuration value!" )
                continue
            
            if( key in self.sub_configurables ):
                self.sub_configurables[key].register_values( vals[ key ] )
        
        return

