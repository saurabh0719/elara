# Add some tests here

import unittest
import elara
import time


class RunTests(unittest.TestCase):
    def setUp(self):
        cache_param = {"max_age": 2, "max_size": 2}
        self.db = elara.exe_cache("test.db", cache_param)

    def test_exe_cache(self):
        cache_param = {"max_age": -1, "max_size": 2}
        with self.assertRaises(Exception):
            new_db = elara.exe_cache("new.db", cache_param)

    def test_age(self):
        self.db.set("key1", 1)
        self.assertEqual(self.db.get("key1"), 1)
        time.sleep(2)
        self.assertEqual(self.db.get("key1"), None)

        self.db.set("key2", 2)
        self.assertEqual(self.db.get("key2"), 2)
        time.sleep(1)
        self.assertEqual(self.db.get("key2"), 2)
        time.sleep(1)
        self.assertEqual(self.db.get("key1"), None)

    def test_size(self):
        self.db.set("key1", 1, "i")
        self.db.set("key2", 2, "i")

        time.sleep(2)
        self.assertEqual(self.db.get("key2"), 2)
        self.db.set("key3", 3)
        time.sleep(2)

        self.assertEqual(self.db.get("key3"), None)
        self.assertEqual(self.db.get("key1"), None)
        self.assertEqual(self.db.get("key2"), 2)

    def test_getkeys(self):
        self.db.set("key1", 1, "i")
        self.db.set("key2", 2, "i")
        self.db.set("key3", 3)
        self.assertEqual(self.db.getkeys(), ["key3", "key2"])
        time.sleep(2)
        self.assertEqual(self.db.getkeys(), ["key2"])

    def test_cache_defaults(self):
        db_new = elara.exe_cache("cache.db", {"max_size": 4})
        db_new.set("key1", 1)
        db_new.set("key2", 2)
        db_new.set("key3", 3)
        db_new.set("key4", 4)

        assert db_new.getkeys() == ["key4", "key3", "key2", "key1"]
        db_new.set("key5", 5, 2)
        assert db_new.getkeys() == ["key5", "key4", "key3", "key2"]

        time.sleep(2)
        assert db_new.getkeys() == ["key4", "key3", "key2"]

        db_new.clear()

        db_new = elara.exe_cache("cache2.db", {"max_size": 4, "cull_freq": 50})

        db_new.set("key1", 1)
        db_new.set("key2", 2)
        db_new.set("key3", 3)
        db_new.set("key4", 4)

        db_new.set("key5", 5)

        assert db_new.getkeys() == ["key5", "key4", "key3"]

    def test_overwrite(self):
        cache_param = {"max_age": 900, "max_size": 4, "cull_freq": 25}

        cache = elara.exe_cache("new.db", cache_param)

        cache.set("key1", "This one will be evicted in 900 seconds")
        cache.set(
            "key2", "This one will not be evicted", "i"
        )  # 'i' signifies it will never be evicted
        cache.set("key3", "This one will be evicted in 100 seconds", 2)

        assert cache.getkeys() == ["key3", "key2", "key1"]
        time.sleep(2)
        assert cache.getkeys() == ["key2", "key1"]

        cache.set("key3", 5)
        cache.set("key4", 1)

        assert cache.getkeys() == ["key4", "key3", "key2", "key1"]

        cache.set("key1", 7, "i")  # overwrite "key1" to never expire

        assert cache.getkeys() == ["key1", "key4", "key3", "key2"]
        assert cache.get("key1") == 7

        cache.set("key5", 20)  # Automatic culling when max_size is reached

        assert cache.getkeys() == ["key5", "key1", "key4", "key3"]
