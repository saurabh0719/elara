"""
Copyright (c) 2021, Saurabh Pujari
All rights reserved.

This source code is licensed under the BSD-style license found in the LICENSE file in the root directory of this source tree.
"""

import datetime
import math
from .status import Status


class Cache_obj:
    def __init__(self, key, max_age=None):
        self.key = key
        if max_age is None:
            self.expiry = None
        else:
            self.expiry = datetime.datetime.now() + datetime.timedelta(seconds=max_age)


class LRU:
    def __init__(self, max_size=math.inf) -> None:
        self.cache = []
        self.size = 0
        # max_size needs to be verified in Elara() to automatically call cull()
        self.max_size = max_size

    # Load LRU everytime DB is loaded
    # Set max_age to the default class max_age
    def _load(self, db, max_age):
        for key in db.keys():
            cache_obj = Cache_obj(key, max_age)
            self.push(cache_obj)

    def _get_cache_object(self, key):
        for i in range(0, self.size):
            if self.cache[i].key == key:
                return self.cache[i]
        return False

    def _resolve_size(self):
        if self.size < self.max_size:
            return True
        else:
            return Status.FULL

    def _ttl(self, key):
        cache_obj = self._get_cache_object(key)
        if cache_obj.expiry is not None:
            delta = cache_obj.expiry - datetime.datetime.now()
            if delta <= datetime.timedelta(seconds=1):
                return datetime.timedelta()
            else:
                return delta
        else:
            return None

    def _persist(self, key):
        cache_obj = Cache_obj(key, None)
        self.push(cache_obj)

    def delete_if_expired(self, key):
        cache_obj = self._get_cache_object(key)

        if not cache_obj:
            return Status.NOTFOUND
        if cache_obj.expiry is None:
            return False
        if cache_obj.expiry <= datetime.datetime.now():
            self.rem(cache_obj)
            return Status.EXPIRED
        else:
            return False

    # Push a new key into the cache
    # IF key already exists then overwrite it
    def push(self, new_cache_obj):
        cache_obj = self._get_cache_object(new_cache_obj.key)

        # If cache_obj is not present, resolve size before pushing
        if cache_obj == False:
            resolve = self._resolve_size()
            if resolve == Status.FULL:
                return Status.FULL
            else:
                self.cache.insert(0, new_cache_obj)
                self.size += 1
                return True
        # If its present, simply delete it and push the new_cache_obj
        else:
            self.rem(cache_obj)
            self.cache.insert(0, new_cache_obj)
            self.size += 1
            return True

    # Pop the least recently used key (end of the cache list)
    def pop(self):
        if self.size == 0:
            return False
        else:
            cache_obj = self.cache[-1]
            del self.cache[-1]
            self.size -= 1
            return cache_obj

    def rem_key(self, key):
        cache_obj = self._get_cache_object(key)
        if cache_obj == False:
            return Status.NOTFOUND
        self.rem(cache_obj)

    def rem(self, cache_obj):
        if cache_obj in self.cache:
            self.cache.remove(cache_obj)
            self.size -= 1
        else:
            return False

    # Peek the most recently used key (start of the cache list)
    def peek(self):
        if self.delete_if_expired(self.cache[0]) == Status.EXPIRED:
            return Status.EXPIRED
        else:
            return self.cache[0]

    # return a list of keys to delete and the remaining cache
    def all(self):
        deleted_keys = []
        for cache_obj in self.cache:
            key = cache_obj.key
            if self.delete_if_expired(cache_obj.key) == Status.EXPIRED:
                deleted_keys.append(key)
        return deleted_keys, self.cache

    # Bring key to the front of the cache
    # Take key as an argument and retrieve the cache_obj
    def touch(self, key):

        res = self.delete_if_expired(key)

        if res == Status.EXPIRED:
            return Status.EXPIRED
        elif res == Status.NOTFOUND:
            return Status.NOTFOUND

        cache_obj = self._get_cache_object(key)

        if self.cache[0] == cache_obj:
            return True
        else:
            self.cache.remove(cache_obj)
            self.size -= 1
            self.push(cache_obj)
            return True

    def clear(self):
        self.cache = []
        self.size = 0

    def print(self):
        print(self.cache)
