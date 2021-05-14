# Add tests here

import unittest
import elara


class RunTests(unittest.TestCase):
    def setUp(self):
        self.db = elara.exe("test.db", False)

    def test_exe(self):
        res = elara.exe("test.db", False)
        assert res is not None

    def test_store_restore_data(self):
        db = elara.exe("test.db")
        db.set("test_key", "test_data:\"ði ıntəˈnæʃənəl fəˈnɛtık əsoʊsiˈeıʃn Y [ˈʏpsilɔn], Yen [jɛn], Yoga [ˈjoːgɑ]\"")
        db.commit()
        db_load = elara.exe("test.db")
        recov_data = db.get("test_key")
        self.assertEqual(recov_data,
                         "test_data:\"ði ıntəˈnæʃənəl fəˈnɛtık əsoʊsiˈeıʃn Y [ˈʏpsilɔn], Yen [jɛn], Yoga [ˈjoːgɑ]\"")

    def test_store_restore_data_secure(self):
        db = elara.exe_secure("test_enc.db")
        db.set("test_key", "test_data:\"ði ıntəˈnæʃənəl fəˈnɛtık əsoʊsiˈeıʃn Y [ˈʏpsilɔn], Yen [jɛn], Yoga [ˈjoːgɑ]\"")
        db.commit()
        db_load = elara.exe_secure("test_enc.db")
        recov_data = db.get("test_key")
        self.assertEqual(recov_data,
                         "test_data:\"ði ıntəˈnæʃənəl fəˈnɛtık əsoʊsiˈeıʃn Y [ˈʏpsilɔn], Yen [jɛn], Yoga [ˈjoːgɑ]\"")

    def test_get(self):
        self.db.db["key"] = "test"
        res = self.db.db["key"]
        self.assertEqual(res, "test")

    def test_set(self):
        self.db.set("key", "test")
        self.assertEqual(self.db.get("key"), "test")

    def test_rem(self):
        self.db.set("key", "test")
        assert "key" in self.db.db
        self.db.rem("key")
        assert "key" not in self.db.db

    def test_clear(self):
        self.db.set("key", "test")
        self.assertEqual(self.db.clear(), True)
        self.assertEqual(self.db.db, {})

    def test_cull(self):
        self.db.set("one", 1)
        self.db.set("two", 2)
        self.db.set("three", 3)
        self.db.set("four", 4)
        self.db.cull(25)
        self.assertEqual(len(self.db.retmem()), 3)
        self.db.cull(100)
        self.assertEqual(len(self.db.retmem()), 0)
        self.assertEqual(self.db.cull(-1), False)
        self.assertEqual(self.db.cull(101), False)

    def test_incr(self):
        self.db.set("one", 1)
        self.db.incr("one")
        self.assertEqual(self.db.get("one"), 2)
        self.db.incr("one", 3.6)
        self.assertEqual(self.db.get("one"), 5.6)
        self.db.incr("one", 0.0003)
        self.assertEqual(self.db.get("one"), 5.600)
        self.db.incr("one", -1)
        self.assertEqual(self.db.get("one"), 4.600)

    def test_decr(self):
        self.db.set("one", 1.35)
        self.db.decr("one")
        self.assertEqual(self.db.get("one"), 0.35)
        self.db.decr("one")
        self.assertEqual(self.db.get("one"), -0.65)
