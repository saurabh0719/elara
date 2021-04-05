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

# Add String specific functions

def SETNX(self, key, data):
    if not self.EXISTS(key):
        self.SET(key, data)
    return True

def APPEND(self, key, data):
    value = self.db[key]
    self.db[key] = value + data
    self._dumpJSON()
    return True

def EXISTS(self, key):
    return key in self.db

def GETSET(self, key, data):
    old_data = self.db[key]
    self.SET(key, data)
    return old_data

def MGET(self, keys):
    result = []
    for key in keys:
        if self.EXISTS(key):
            result.append(self.GET(key))
    return result

def MSET(self, dict):
    for key in dict:
        self.SET(key, dict[key])
    return True

def MSETNX(self, dict):
    for key in dict:
        if not self.EXISTS(key):
            self.SET(key, dict[key])
    return True  

def SLEN(self, key):
    if self.EXISTS(key):
        return len(self.db[key])
    return -1
