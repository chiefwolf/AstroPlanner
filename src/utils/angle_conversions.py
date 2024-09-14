# chief_wolf
# 9/13/2024
# See LICENSE in root directory for license information

from typing import *
import math

def degree_minute_second_to_float( input:str ) -> float:
    angle:float = 0
    curr_str:str = ''

    for val in input:
        if not( ( val == 'd' ) or ( val == '\'' ) or ( val == '"' ) ):
            curr_str += val
        else:
            if( val == 'd' ):
                angle = float( curr_str ) * math.pi / 180
                
                curr_str = ''
            
            elif( val == '\'' ):
                if( angle >= 0 ):
                    angle += float( curr_str ) / 60.0 * math.pi / 180
                else:
                    angle -= float( curr_str ) / 60.0 * math.pi / 180
                
                curr_str = ''
            
            elif( val == '\"' ):
                if( angle >= 0 ):
                    angle += float( curr_str ) / 3600 * math.pi / 180
                else:
                    angle -= float( curr_str ) / 3600 * math.pi / 180
                
                curr_str = ''
    
    return angle


def hour_minute_second_to_float( input:str ) -> float:
    angle:float = 0
    curr_str:str = ''

    for val in input:
        if not( ( val == 'h' ) or ( val == 'm' ) or ( val == 's' ) ):
            curr_str += val
        else:
            if( val == 'h' ):
                # An hour is 1/24 of a circle...
                angle = float( curr_str ) * ( 360.0 / 24.0 ) * math.pi / 180 # And convert to radians...
                
                curr_str = ''
            
            elif( val == 'm' ):
                # A minute is 1/60 of an hour...
                if( angle >= 0 ):
                    angle += float( curr_str ) * ( 360.0 / 24.0 / 60.0 ) * math.pi / 180
                else:
                    angle -= float( curr_str ) * ( 360.0 / 24.0 / 60.0 ) * math.pi / 180
                
                curr_str = ''

            
            elif( val == 's' ):
                # A second is 1/3600 of an hour...
                if( angle >= 0 ):
                    angle += float( curr_str ) * ( 360.0 / 24.0 / 3600.0 ) * math.pi / 180
                else:
                    angle -= float( curr_str ) * ( 360.0 / 24.0 / 3600.0 ) * math.pi / 180

                curr_str = ''
    
    return angle

