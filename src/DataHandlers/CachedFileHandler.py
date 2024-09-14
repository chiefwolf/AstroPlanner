# chief_wolf
# 9/12/2024
# See LICENSE in root directory for license information

from typing import *
import traceback
import os

class CachedFileHandler:
    '''
    CachedFileHandler is made to handle casses where the end user may not necessarily want to immediately write data to a file, but instead wait until there is enough output in the cache to write to the file 
    '''
    def __init__( self, file_name:Union[str, bytes, os.PathLike]="simple_file.txt", max_cache_size:int=100, file_mode:str='at' ):
        '''
        file_name: Some path-like location & filename to output the file to
        max_cache_size: Maximum number of entries in the cache until the cache is flushed
        file_mode: How to open the file, default should be fine unless for whatever reason a binary file is wanted
        '''
        self.cache: List[str] = []
        self.max_cache_size: int = max_cache_size
        self.file_name: str =  file_name
        self.file_mode: str = file_mode

    def __del__( self ):
        self.flush_cache( force_flush=True )
    
    def flush_cache( self, force_flush:bool = False ) -> bool:
        '''
        flush_cache will check to see if it should flush this object's cache - can be forced with force_flush = True. Returns true when successful
        '''
        # Make sure that we actually need to flush the files
        if( force_flush or ( len(self.cache) > self.max_cache_size ) ):
            with open( self.file_name, mode=self.file_mode ) as file:
                # Iterate over each line in the cache and actually write it to the file
                for line in self.cache:
                    file.write(f'{line}\n')
                
                file.flush()
        
        return True

    def write( self, line:str ) -> bool:
        '''
        write will add the string to the cache
        '''
        self.cache.append( line )

        self.flush_cache()
