#! /usr/bin/python

# cheif_wolf
# 9/12/2024
# See LICENSE in root directory for license information

import math

from src.utils.angle_conversions import degree_minute_second_to_float

from src.UniverseBuilder.MessierBuilder import MessierBuilder
from src.Logger import Logger

def main():
    print( "Hello World!" )

    genesis = Logger( 'logs/genesis.txt' )

    big_bang = MessierBuilder( 'catalog/simple_messier_list.txt', genesis, 1 )

    celestial_objects = big_bang.get_objects()

    for object in celestial_objects:
        print( f'{object.common_name}:' )
        print( f'\tMD:{object.max_dimension*180/math.pi:3.5f}d')
        print( f'\tRA:{object.right_ascension*180/math.pi:3.5f}d')
        print( f'\t D:{object.declination*180/math.pi:3.5f}d')
        print( '' )


if __name__ == "__main__":
    main()
