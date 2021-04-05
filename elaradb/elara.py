"""
BSD 3-Clause License

Copyright (c) 2021, Saurabh Pujari
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import os
import json
from elarautil import Util

class Elara(object):

    from strings import (SETNX, APPEND, EXISTS, GETSET, MSET, MSETNX, SLEN)

    from lists import (LNEW, LADD, LEXTEND, LINDEX, LRANGE,
                       LDEL, LPOP, LLEN, LAPPEND, LEXISTS, LINSERT)
                       
    from hashtables import (HNEW, HADD, HADDT, HGET, HPOP, HKEYS, HVALS, HEXISTS, HMERGE)

    def __init__(self, path, key_path = None):
        '''Creates a database object and loads the data from the location path.
        If the file does not exist it will be created on the first update.'''
        self.path = os.path.expanduser(path)
        
        if key_path:
            new_key_path = os.path.expanduser(key_path)
            if os.path.exists(new_key_path):
                file = open(new_key_path, 'rb')
                self.key = file.read()
                file.close()
            else:
                self.key = None
        else:
            self.key = None

        if os.path.exists(path):
            self._loadJSON()
        else:
            self.db = {}

    def _loadJSON(self):
        if self.key:
            self.db = Util.readAndDecrypt(self)
        else:
            self.db = json.load(open(self.path, 'rb'))

    def _dumpJSON(self):
        if self.key:
            Util.encryptAndStore(self) # Enclose in try-catch
        else:
            json.dump(self.db, open(self.path, 'wt'))
    
    def SAVE(self):
        self._dumpJSON()
        return True
    
    def SET(self, key, value):
        self.db[key] = value
        self._dumpJSON()
        return True
    
    def GET(self, key):
        try:
            return self.db[key]
        except KeyError:
            return None
    
    def DEL(self, key):
        del self.db[key]
        self._dumpJSON()
        return True
    
    def CLEAR(self):
        self.db = {}
        self._dumpJSON()
        return True