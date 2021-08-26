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


# Hash table operations


def hnew(self, key, max_age=None):
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

    self.db[key] = {}
    self._autocommit()
    return True


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
    if self.exists(key):
        return self.db[key].keys()
    else:
        return None


def hvals(self, key):
    if self.exists(key):
        return self.db[key].values()
    else:
        return None


def hexists(self, key, dict_key):
    if self.exists(key):
        if dict_key in self.db[key]:
            return True
        else:
            return False
    else:
        return False


def hmerge(self, key, new_dict):
    if self.exists(key):
        first = self.db[key]
        first.update(new_dict)
        self._autocommit()
        return True
    else:
        return False
