# Add tests here

from typing import List
import unittest
import elara


class RunTests(unittest.TestCase):
    def setUp(self):
        self.db = elara.exe("test.db", False)
        self.db.hnew("newmap")

    def test_hnew(self):
        with self.assertRaises(Exception):
            self.db.hnew("key", -1)

    def test_hadd(self):
        self.assertEqual(len(self.db.get("newmap")), 0)
        self.db.hadd("newmap", "one", 1)
        self.assertEqual(len(self.db.get("newmap")), 1)

        self.assertEqual(self.db.hadd("newmap1", "two", 2), False)
        new_map = self.db.get("newmap")
        self.assertEqual(new_map["one"], 1)
        self.db.hadd("newmap", "string", "text")
        new_map = self.db.get("newmap")
        self.assertEqual(new_map["string"], "text")

    def test_haddt(self):
        self.db.haddt("newmap", ("one", 1))
        self.assertEqual(self.db.get("newmap")["one"], 1)
        self.db.haddt("newmap", ("two", 2))
        self.assertEqual(len(self.db.get("newmap")), 2)

    def test_hget(self):
        self.db.haddt("newmap", ("one", 1))
        self.assertEqual(self.db.hget("newmap", "one"), 1)
        self.assertEqual(self.db.hget("newmap1", "two"), False)

    def test_hpop(self):
        self.db.haddt("newmap", ("one", 1))
        self.db.haddt("newmap", ("two", 2))
        self.assertEqual(self.db.hpop("newmap", "one"), 1)
        self.assertEqual(self.db.hpop("newmap1", "one"), False)

    def test_hkeys(self):
        self.db.haddt("newmap", ("one", 1))
        self.db.haddt("newmap", ("two", 2))
        assert "one" in self.db.hkeys("newmap")
        assert len(self.db.hkeys("newmap")) == 2

    def test_hvals(self):
        self.db.haddt("newmap", ("one", "demo"))
        self.db.haddt("newmap", ("two", 2))
        assert "demo" in self.db.hvals("newmap")
        assert 2 in self.db.hvals("newmap")
        assert len(self.db.hvals("newmap")) == 2

    def test_hexists(self):
        self.db.haddt("newmap", ("one", "demo"))
        self.db.haddt("newmap", ("two", 2))
        self.assertEqual(self.db.hexists("newmap", "one"), True)
        self.assertEqual(self.db.hexists("newmap", "three"), False)
        self.assertEqual(self.db.hexists("newmap1", "one"), False)

    def test_hmerge(self):
        self.db.hadd("newmap", "one", 1)
        self.db.hadd("newmap", "two", 2)
        self.assertEqual(len(self.db.get("newmap")), 2)
        new_dict = {"two": 20, "three": 3}
        self.db.hmerge("newmap", new_dict)
        self.assertEqual(len(self.db.get("newmap")), 3)
        self.assertEqual(self.db.get("newmap")["two"], 20)
