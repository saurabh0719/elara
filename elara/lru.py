'''
Copyright (c) 2021, Saurabh Pujari
All rights reserved.

This source code is licensed under the BSD-style license found in the LICENSE file in the root directory of this source tree.
'''

import sys

class LRU():
    
    def __init__(self, size=sys.maxint) -> None:
        self.cache = []
        self.size = size
    
    # Push a new key into the cache  
    def push(self, key):
        pass
    
    # Pop the least recently used key (end of the cache list)
    def pop(self):
        pass
    
    # Peek the most recently used key (start of the cache list)
    def peek(self):
        pass
    
    # Bring key to the front of the cache 
    def touch(self, key):
        pass

    # Delete `count` numbner of least recently used keys
    def cull(self, count=1):
        pass
    
