"""
Copyright (c) 2021, Saurabh Pujari
All rights reserved.

This source code is licensed under the BSD-style license found in the LICENSE file in the root directory of this source tree.
"""

import random

def randomkey(self):
    # get all un-expired keys
    keys = self.getkeys()
    if keys is None:
        return None
    return random.choice(keys)

# get time to live in datetime format of any key
def ttl(self, key):
    if self.exists(key):
        return self.lru._ttl(key)
    else:
        return False

# get time to live in seconds of any key
def ttls(self, key):
    if self.exists(key):
        delta = self.lru._ttl(key)
        if delta is not None:
            return delta.total_seconds()
        return delta
    else:
        return False

# persist any key permanently 
def persist(self, key):
    if self.exists(key):
        self.lru._persist(key)
    else:
        return False