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

# Add list specific functions

def LNEW(self, key):
    self.db[key] = []
    self._dumpJSON()
    return True

def LADD(self, key, value):
    self.db[key].append(value)
    self._dumpJSON()
    return True

def LEXTEND(self, key, seq):
    self.db[key].extend(seq)
    self._dumpJSON()
    return True

def LINDEX(self, key, index):
    return self.db[key][index]

def LRANGE(self, key, start=None, end=None):
    return self.db[key][start:end]

def LDEL(self, key, value):
    self.db[key].remove(value)
    self._dumpJSON()
    return True

def LPOP(self, key, pos):
    value = self.db[key][pos]
    del self.db[key][pos]
    self._dumpJSON()
    return value

def LLEN(self, key):
    return len(self.db[key])

def LAPPEND(self, key, pos, more):
    tmp = self.db[key][pos]
    self.db[key][pos] = tmp + more
    self._dump()
    return True

def LEXISTS(self, key, value):
    # modify and return index
    return value in self.db[key]

def LINSERT(self, key, value, index):
    pass