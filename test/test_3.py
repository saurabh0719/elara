# Add tests here

import unittest
import elara


class RunTests(unittest.TestCase):
    def setUp(self):
        self.db = elara.exe("test.db", False)
        self.db.lnew("newlist")

    def test_lnew(self):
        with self.assertRaises(Exception):
            self.db.lnew("key", -1)

    def test_lpush(self):
        self.assertEqual(len(self.db.get("newlist")), 0)
        self.db.lpush("newlist", 3)
        self.assertEqual(len(self.db.get("newlist")), 1)
        self.db.lpush("newlist", 4)
        self.assertEqual(len(self.db.get("newlist")), 2)
        new_list = self.db.get("newlist")
        self.assertEqual(new_list[1], 4)
        self.db.lpush("newlist", "string")
        new_list = self.db.get("newlist")
        self.assertEqual(new_list[2], "string")

    def test_lextend(self):
        self.db.lpush("newlist", 3)
        self.assertEqual(len(self.db.get("newlist")), 1)
        new_list = [4, 5]
        self.assertEqual(self.db.lextend("newlist", new_list), True)
        self.assertEqual(len(self.db.get("newlist")), 3)
        self.assertEqual(self.db.lextend("newlist2", new_list), False)

    def test_lindex(self):
        self.db.lpush("newlist", 3)
        new_list = [4, 5]
        self.assertEqual(self.db.lextend("newlist", new_list), True)
        self.assertEqual(self.db.lindex("newlist", 0), 3)
        self.assertEqual(self.db.lindex("newlist", 5), False)

    def test_lrange(self):
        new_list = [4, 5, 6, 7, 8, 9]
        self.assertEqual(self.db.lextend("newlist", new_list), True)
        self.assertEqual(self.db.lrange("newlist", 2, 4), [6, 7])
        self.assertEqual(self.db.lrange("newlist", 10, 20), [])

    def test_lrem(self):
        new_list = ["cat", "dog", "bird"]
        self.assertEqual(self.db.lextend("newlist", new_list), True)
        self.assertEqual(self.db.lrem("newlist", "dog"), True)
        self.assertEqual(self.db.lrem("newlist", 20), False)

    def test_lpop(self):
        new_list = [4, 5, 6, 7, 8, 9]
        self.assertEqual(self.db.lextend("newlist", new_list), True)
        self.assertEqual(self.db.lpop("newlist", -2), False)
        self.assertEqual(self.db.lpop("newlist"), 9)
        self.assertEqual(len(self.db.get("newlist")), len(new_list) - 1)
        self.assertEqual(self.db.lpop("list"), False)

    def test_llen(self):
        new_list = [4, 5, 6, 7, 8, 9]
        self.assertEqual(self.db.lextend("newlist", new_list), True)
        self.assertEqual(self.db.llen("newlist"), len(new_list))
        self.assertEqual(self.db.llen("list"), -1)

    def test_lappend(self):
        new_list = [4, 5, 6, 7, 8, 9]
        self.assertEqual(self.db.lextend("newlist", new_list), True)
        self.assertEqual(self.db.lappend("newlist", 0, 3), True)
        self.assertEqual(self.db.lindex("newlist", 0), 7)
        self.assertEqual(self.db.lappend("list", 0, 3), False)

    def test_lexists(self):
        new_list = [4, 5, 6, 7, 8, 9]
        self.assertEqual(self.db.lextend("newlist", new_list), True)
        self.assertEqual(self.db.lexists("newlist", 5), True)
        self.assertEqual(self.db.lexists("newlist", 20), False)
        self.assertEqual(self.db.lexists("list", 0), False)
