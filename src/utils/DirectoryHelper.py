# chief_wolf
# 9/20/2024
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

class DirectoryHelper():
    '''
    DirectoryHelper is a helper class that is meant to replace aliases with the true path. 
    Hardcoded for now, but can be easily made into a dictionary-based system.
    '''
    def __init__( self, workspace_str:str="${workspace}", config_str:str="${configs}", catalog_str:str ="${catalogs}", log_str:str="${logs}"  ):
        self.workspace_str: str = workspace_str
        self.config_str: str    = config_str
        self.catalog_str:str    = catalog_str
        self.log_str:str        = log_str

        self.workspace_dir:os.PathLike  = os.path.normpath( os.path.split(__file__)[0] + '../../..' )
        self.config_dir:os.PathLike     = os.path.normpath( self.workspace_dir + '/config' )
        self.catalog_dir:os.PathLike    = os.path.normpath( self.workspace_dir + '/catalog' )
        self.log_dir:os.PathLike        = os.path.normpath( self.workspace_dir + '/logs' )

    def replace_alias_strings( self, in_str: str ) -> str:
        '''
        Search for aliases in the file and replace them with the proper path
        '''
        out_str = in_str
        if( self.workspace_str in out_str ):
            out_str = out_str.replace( self.workspace_str, self.workspace_dir )
        
        if( self.config_str in out_str ):
            out_str = out_str.replace( self.config_str, self.config_dir )

        if( self.catalog_str in out_str ):
            out_str = out_str.replace( self.catalog_str, self.catalog_dir )
        
        out_str = os.path.normpath( out_str )
        
        return out_str
    
    def replace_dir_strings( self, in_str: str ) -> str:
        '''
        Search for a directory string and replace it with their alias
        '''

        out_str = in_str
        if( self.catalog_dir in out_str ):
            out_str = out_str.replace( self.catalog_dir, self.catalog_str )
        elif( self.config_dir in out_str ):
            out_str = out_str.replace( self.config_dir, self.config_str )
        elif( self.workspace_dir in out_str ):
            out_str = out_str.replace( self.workspace_dir, self.workspace_str )

        return out_str
    