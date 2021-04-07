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
from .elarautil import Util
from .shared import SharedOp
from .lists import ListOp
from .hashtables import HashtableOp
from .strings import StringOp

class Elara(SharedOp, StringOp, ListOp, HashtableOp):

    # from strings import (setnx, append, getset, mset, msetnx, slen)
    # from lists import (lnew, ladd, lextend, lindex, lrange, lrem, lpop, llen, lappend, lexists, linsert)
    # from hashtables import (hnew, hadd, haddt, hget, hpop, hkeys, hvals, hexists, hmerge)
    # from shared import (retall, retdb, retkey, commit, exists)

    def __init__(self, path, commitdb, key_path = None):
        self.path = os.path.expanduser(path)
        self.commitdb = commitdb

        # Load the database key
        if not key_path==None:
            new_key_path = os.path.expanduser(key_path)
            if os.path.exists(new_key_path):
                file = open(new_key_path, 'rb')
                self.key = file.read()
                file.close()
            else:
                self.key = None
        else:
            self.key = None

        # Load the data
        if os.path.exists(path):
            self._load()
        else:
            self.db = {}

    def _load(self):
        if self.key:
            self.db = Util.readAndDecrypt(self)
        else:
            self.db = Util.readJSON(self)

    def _dump(self):
        if self.key:
            Util.encryptAndStore(self) # Enclose in try-catch
        else:
            Util.storeJSON(self)

    def _autocommit(self):
        if self.commitdb:
            self._dump()
    
    def set(self, key, value):
        self.db[key] = value
        self._autocommit()
        return True
    
    def get(self, key):
        try:
            return self.db[key]
        except KeyError:
            return None
    
    def rem(self, key):
        del self.db[key]
        self._autocommit()
        return True
    
    def clear(self):
        self.db = {}
        self._autocommit()
        return True