# chief_wolf
# 9/13/2024
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

