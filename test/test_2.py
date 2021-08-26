# Add tests here

import unittest
import elara


class RunTests(unittest.TestCase):
    def setUp(self):
        self.db = elara.exe("test.db", False)

    def test_setnx(self):
        self.db.set("key1", "value1")
        self.assertEqual(self.db.setnx("key1", "value"), False)
        self.assertEqual(self.db.setnx("key", "value"), True)
        self.assertEqual(self.db.setnx("key", "value"), False)

    def test_append(self):
        self.db.set("key", "value")
        self.assertEqual(self.db.append("key", "data"), "valuedata")
        self.assertEqual(self.db.append("key", 1), False)

    def test_getset(self):
        self.db.set("key", "value")
        self.assertEqual(self.db.getset("key", "newvalue"), "value")
        self.assertEqual(self.db.getset("key", 1), "newvalue")
        self.assertEqual(self.db.get("key"), 1)

        self.assertEqual(self.db.getset("keynotfound", 1), False)
        with self.assertRaises(Exception):
            self.db.getset("key", 5, -1)

    def test_mget(self):
        self.db.set("key", "value")
        self.db.set("key1", 3)
        keys = ["key", "key1", "key2"]
        self.assertEqual(self.db.mget(keys), ["value", 3])
        self.db.set("key2", "value2")
        self.assertEqual(self.db.mget(keys), ["value", 3, "value2"])
        self.assertNotEqual(self.db.mget(keys), ["value", "value2", 3])

    def test_mset(self):
        new_dict = {"key1": [1, 2, 3], 1: "value", "key2": "value2"}
        self.db.mset(new_dict)
        self.assertEqual(self.db.mget(["key1", 1]), [[1, 2, 3], "value"])

    def test_msetnx(self):
        self.db.set("key", "value")
        new_dict = {"key": [1, 2, 3], "key2": "value2", "key3": "value3"}
        self.db.msetnx(new_dict)
        self.assertEqual(
            self.db.mget(["key", "key3", "key2"]), ["value", "value3", "value2"]
        )
