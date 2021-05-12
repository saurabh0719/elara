"""
Copyright (c) 2021, Saurabh Pujari
All rights reserved.

This source code is licensed under the BSD-style license found in the LICENSE file in the root directory of this source tree.
"""


class LRU:
    def __init__(self) -> None:
        self.cache = []
        self.size = 0

    # Push a new key into the cache
    def push(self, key):
        if key in self.cache:
            self.touch(key)
        else:
            self.cache.insert(0, key)
            self.size += 1

    # Pop the least recently used key (end of the cache list)
    def pop(self):
        if len(self.cache) == 0:
            return False
        else:
            val = self.cache[-1]
            del self.cache[-1]
            self.size -= 1
            return val

    def rem(self, key):
        if key in self.cache:
            self.cache.remove(key)
            self.size -= 1
        else:
            return False

    # Peek the most recently used key (start of the cache list)
    def peek(self):
        return self.cache[0]

    def all(self):
        return self.cache

    # Bring key to the front of the cache
    def touch(self, key):
        if key in self.cache:
            if self.cache[0] == key:
                pass
            else:
                self.cache.remove(key)
                self.push(key)
        else:
            return False

    def clear(self):
        self.cache = []
        self.size = 0

    def print(self):
        print(self.cache)
