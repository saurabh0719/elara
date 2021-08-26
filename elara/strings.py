"""
Copyright (c) 2021, Saurabh Pujari
All rights reserved.

This source code is licensed under the BSD-style license found in the LICENSE file in the root directory of this source tree.
"""


def is_pos(val):
    return isinstance(val, int) and val > 0


# Add String specific functions


def setnx(self, key, data):
    if not self.exists(key):
        self.set(key, data)
        return True
    else:
        return False


def append(self, key, data):
    if self.exists(key):
        if isinstance(data, str):
            value = self.db[key]
            self.db[key] = value + data
            self._autocommit()
            return self.db[key]
        else:
            return False
    else:
        return False


def getset(self, key, data, max_age=None):
    if self.exists(key):
        old_data = self.db[key]
    else:
        return False
    self.set(key, data, max_age)
    return old_data


def mget(self, keys):
    result = []
    for key in keys:
        if self.exists(key):
            result.append(self.get(key))
    return result


def mset(self, dict):
    for key in dict:
        self.set(key, dict[key])
    return True


def msetnx(self, dict):
    for key in dict:
        self.setnx(key, dict[key])
    return True


def slen(self, key):
    if self.exists(key):
        return len(self.db[key])
    return -1
