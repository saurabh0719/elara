"""
Copyright (c) 2021, Saurabh Pujari
All rights reserved.

This source code is licensed under the BSD-style license found in the LICENSE file in the root directory of this source tree.
"""


from .lru import Cache_obj
from .status import Status
from .exceptions import InvalidCacheParams


def is_pos(val):
    return isinstance(val, int) and val > 0


# Add list specific functions


def lnew(self, key, max_age=None):
    if max_age == None:
        cache_obj = Cache_obj(key, self.max_age)
    else:
        if is_pos(max_age):
            cache_obj = Cache_obj(key, max_age)
        else:
            raise InvalidCacheParams("max_age")

    if self.lru.push(cache_obj) == Status.FULL:
        self.cull(self.cull_freq)  # Automatic cull
        self.lru.push(cache_obj)

    self.db[key] = []
    self._autocommit()
    return True


def lpush(self, key, value):
    if self.exists(key):
        self.db[key].append(value)
        self._autocommit()
        return True
    else:
        return False


def lextend(self, key, list_data):
    if self.exists(key):
        self.db[key].extend(list_data)
        self._autocommit()
        return True
    else:
        return False


def lindex(self, key, index):
    if self.exists(key) and len(self.db[key]) > index:
        return self.db[key][index]
    else:
        return False


def lrange(self, key, start=None, end=None):
    if self.exists(key):
        return self.db[key][start:end]
    else:
        return False


def lrem(self, key, value):
    if self.exists(key) and len(self.db[key]) > 0:
        try:
            self.db[key].remove(value)
        except ValueError:
            return False
        self._autocommit()
        return True
    else:
        return False


def lpop(self, key, pos=-1):
    len = self.llen(key)
    if self.exists(key) and pos < len:
        if pos < -1:
            return False
        else:
            value = self.db[key][pos]
            del self.db[key][pos]
            self._autocommit()
            return value
    else:
        return False


def llen(self, key):
    if self.exists(key):
        return len(self.db[key])
    else:
        return -1


def lappend(self, key, pos, more):
    if self.exists(key):
        try:
            tmp = self.db[key][pos]
            self.db[key][pos] = tmp + more
        except:
            return False
        self._autocommit()
        return True
    else:
        return False


def lexists(self, key, value):
    # modify and return index
    if self.exists(key):
        return value in self.db[key]
    else:
        return False


def linsert(self, key, value, index):
    if self.exists(key) and isinstance(self.db[key], list):
        self.db[key].insert(index, value)
    else:
        return False
