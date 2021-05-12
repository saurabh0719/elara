"""
Copyright (c) 2021, Saurabh Pujari
All rights reserved.

This source code is licensed under the BSD-style license found in the LICENSE file in the root directory of this source tree.
"""

# Hash table operations

def hnew(self, key):
    if isinstance(key, str):
        self.db[key] = {}
        self.lru.push(key)
        self._autocommit()
        return True
    else:
        raise Exception

def hadd(self, key, dict_key, value):
    if self.exists(key):
        self.db[key][dict_key] = value
        self._autocommit()
        return True
    else:
        return False

def haddt(self, key, tuple):
    if self.exists(key):
        self.db[key][tuple[0]] = tuple[1]
        self._autocommit()
        return True
    else:
        return False

def hget(self, key, dict_key):
    if self.exists(key):
        return self.db[key][dict_key]
    else:
        return False

def hpop(self, key, dict_key):
    if self.exists(key):
        value = self.db[key][dict_key]
        del self.db[key][dict_key]
        self._autocommit()
        return value
    else:
        return False

def hkeys(self, key):
    self.lru.touch(key)
    return self.db[key].keys()

def hvals(self, key):
    self.lru.touch(key)
    return self.db[key].values()

def hexists(self, key, dict_key):
    self.lru.touch(key)
    return dict_key in self.db[key]

def hmerge(self, key, new_dict):
    self.lru.touch(key)
    first = self.db[key]
    first.update(new_dict)
    self._autocommit()
    return True