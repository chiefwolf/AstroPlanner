#! /usr/bin/python

# cheif_wolf
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

import math

from src.utils.angle_conversions import degree_minute_second_to_float

from src.UniverseBuilder.MessierBuilder import MessierBuilder
from src.Logger import Logger
from src.ConfigHandler import ConfigHandler
from src.utils.DirectoryHelper import DirectoryHelper

def main():
    print( "Hello World!" )

    genesis = Logger( 'logs/genesis.txt' )

    dir_helper = DirectoryHelper()

    universal_constants = ConfigHandler( dir_helper, genesis )

    big_bang = MessierBuilder( 'catalog/simple_messier_list.txt', genesis, 1 )

    universal_constants.register_configurable( big_bang )

    celestial_objects = big_bang.get_objects()
    
    universal_constants.write_config()

    for object in celestial_objects:
        print( f'{object.common_name}:' )
        print( f'\tMD:{object.max_dimension*180/math.pi:3.5f}d')
        print( f'\tRA:{object.right_ascension*180/math.pi:3.5f}d')
        print( f'\t D:{object.declination*180/math.pi:3.5f}d')
        print( '' )


if __name__ == "__main__":
    main()
