# Add tests here

import unittest
from elara import LRU, Cache_obj


class RunTests(unittest.TestCase):
    def setUp(self):
        self.lru = LRU()
        self.tiny_lru = LRU(2)  # Set max_size of the cache
        self.obj1 = Cache_obj("key1")
        self.obj2 = Cache_obj("key2")
        self.lru.push(self.obj1)
        self.lru.push(self.obj2)

    def test_push(self):
        deleted_keys, cache = self.lru.all()
        self.assertEqual(len(deleted_keys), 0)
        x = []
        # append in reverse order to match cache lru
        x.append(self.obj2)
        x.append(self.obj1)
        self.assertEqual(cache, x)

    def test_peek(self):
        self.assertEqual(self.lru.peek(), self.obj2)

    def test_touch(self):
        self.lru.touch(self.obj1.key)
        self.assertEqual(self.lru.peek(), self.obj1)

    def test_clear(self):
        self.lru.clear()
        deleted_keys, cache = self.lru.all()
        self.assertEqual(len(deleted_keys), 0)
        self.assertEqual(len(cache), 0)

    def test_rem(self):
        self.lru.rem(self.obj2)
        deleted_keys, cache = self.lru.all()
        self.assertEqual(cache[0], self.obj1)

    def test_pop(self):
        self.assertEqual(self.lru.pop(), self.obj1)
        deleted_keys, cache = self.lru.all()
        self.assertEqual(len(deleted_keys), 0)
        self.assertEqual(len(cache), 1)
