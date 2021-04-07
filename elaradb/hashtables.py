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

# Add hash/Dictionary specific functions
class HashtableOp():
    def hnew(self, key):
        if isinstance(key, str):
            self.db[key] = {}
            self._autocommit()
            return True
        else:
            raise Exception

    def hadd(self, key, dict_key, value):
        self.db[key][dict_key] = value
        self._autocommit()
        return True

    def haddt(self, key, tuple):
        self.db[key][tuple[0]] = tuple[1]
        self._autocommit()
        return True

    def hget(self, key, dict_key):
        return self.db[key][dict_key]

    def hpop(self, key, dict_key):
        value = self.db[key][dict_key]
        del self.db[key][dict_key]
        self._autocommit()
        return value

    def hkeys(self, key):
        return self.db[key].keys()

    def hvals(self, key):
        return self.db[key].values()

    def hexists(self, key, dict_key):
        return dict_key in self.db[key]

    def hmerge(self, key1, key2):
        first = self.db[key1]
        second = self.db[key2]
        first.update(second)
        self._autocommit()
        return True