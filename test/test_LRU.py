# Add tests here 

import unittest
from elara import LRU

class RunTests(unittest.TestCase):
    def setUp(self):
        self.lru = LRU()
        self.lru.push('key1')
        self.lru.push('key2')
        
    def test_push(self):
        self.assertEqual(self.lru.all(), ['key2', 'key1'])
        
    def test_peek(self):
        self.assertEqual(self.lru.peek(), 'key2')
        
    def test_touch(self):
        self.lru.touch('key1')
        self.assertEqual(self.lru.peek(), 'key1')
        
    def test_clear(self):
        self.lru.clear()
        self.assertEqual(self.lru.all(), [])
        
    def test_rem(self):
        self.lru.rem('key2')
        self.assertEqual(self.lru.all(), ['key1'])
    
    def test_pop(self):
        self.assertEqual(self.lru.pop(), 'key1')
        self.assertEqual(len(self.lru.all()), 1)