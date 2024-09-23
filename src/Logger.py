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
import sys
from enum import Enum
import datetime

from src.DataHandlers.CachedFileHandler import CachedFileHandler

class LogLevel(Enum):
    LOG = 0
    WARNING = 1
    ERROR = 2
    NONE = 1e6 # Something ridiculous to always be highest value

    def __lt__( self, other ) -> bool:
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented
    def __le__( self, other ) -> bool:
        if self.__class__ is other.__class__:
            return self.value <= other.value
        return NotImplemented

class Logger:
    '''
    A simple logger that caches its logs until there are enough logs to output
    '''
    def __init__( self, file_name:Union[str, bytes, os.PathLike]='log.txt', log_time:bool=True, print_level:LogLevel=LogLevel.LOG ):
        self.file: CachedFileHandler = CachedFileHandler( file_name=file_name )

        self.log_time: bool = log_time
        self.print_level: LogLevel = print_level
        self.delayed_warning:bool = False

    def _get_time( self ) -> str:
        '''
        _get_time is a private function to return a formatted time in the way that the logger wants
        '''
        if self.log_time:
            return f' [{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}] '
        else:
            return ' '
    
    def log( self, log:str ) -> bool:
        '''
        Log will log the given string to the log file, and to the console if requested at the LOG level
        '''
        log_str = f'[LOG]{self._get_time()}{log}'

        self.file.write( log_str )

        if( self.print_level <= LogLevel.LOG ):
            print( f'{log_str}' )

        return True
    
    def warning( self, log:str ) -> bool:
        '''
        Warning will log the given string to the log file, and to the console if requested at the WARNING level
        '''
        log_str = f'[WARNING]{self._get_time()}{log}'

        self.file.write( log_str )

        if( self.print_level <= LogLevel.WARNING ):
            print( f'{log_str}' ) 
        
        return True
    
    def error( self, log:str, error_code:int ):
        '''
        Error will log the given error to the log file, to the console if requested at ERROR level, and will exit the program with error_code 
        '''
        log_str = f'[ERROR]{self._get_time()}{log}'
        self.file.write( log_str )

        if( self.print_level <= LogLevel.ERROR ):
            print( f'{log_str}' )
        
        sys.exit( error_code )
    
    def delayed_warning( self, log:str ) -> None:
        '''
        Log will be logged as a warning, and can later be used to stop execution of the program
        '''

        self.warning( f'[DELAYED] {log}' )

        self.delayed_warning = True

        return
    
    def execute_delayed_warning( self ) -> None:
        '''
        If the delayed warning flag was set before, error out of the program
        '''
        if( self.delayed_warning == True ):
            self.error( "Delayed warning errored out program, see above in log file for more information", 1 )

        return
