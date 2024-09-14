# chief_wolf
# 9/12/2024
# See LICENSE in root directory for license information

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
        log will log the given string to the log file, and to the console if requested at the LOG level
        '''
        log_str = f'[LOG]{self._get_time()}{log}'

        self.file.write( log_str )

        if( self.print_level <= LogLevel.LOG ):
            print( f'{log_str}' )

        return True
    
    def warning( self, log:str ):
        '''
        warning will log the given string to the log file, and to the console if requested at the WARNING level
        '''
        log_str = f'[WARNING]{self._get_time()}{log}'

        self.file.write( log_str )

        if( self.print_level <= LogLevel.WARNING ):
            print( f'{log_str}' ) 
    
    def error( self, log:str, error_code:int ):
        '''
        error will log the given error to the log file, to the console if requested at ERROR level, and will exit the program with error_code 
        '''
        log_str = f'[ERROR]{self._get_time()}{log}'
        self.file.write( log_str )

        if( self.print_level <= LogLevel.ERROR ):
            print( f'{log_str}' )
        
        sys.exit( error_code )
