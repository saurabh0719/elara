# Add some tests here

import unittest
import elara
import os


class RunTests(unittest.TestCase):
    def setUp(self):
        self.db = elara.exe("test.db", False)

    def test_exe(self):
        res = elara.exe("test.db", False)
        assert res is not None

    def test_store_restore_data(self):
        db = elara.exe("test_store.db")
        db.set(
            "test_key",
            'test_data:"ði ıntəˈnæʃənəl fəˈnɛtık əsoʊsiˈeıʃn Y [ˈʏpsilɔn], Yen [jɛn], Yoga [ˈjoːgɑ]"',
        )
        db.commit()
        db_load = elara.exe("test_store.db")
        recov_data = db_load.get("test_key")
        self.assertEqual(
            recov_data,
            'test_data:"ði ıntəˈnæʃənəl fəˈnɛtık əsoʊsiˈeıʃn Y [ˈʏpsilɔn], Yen [jɛn], Yoga [ˈjoːgɑ]"',
        )
        # cleanup database files
        os.remove("test_store.db")

    def test_store_restore_data_secure(self):
        db = elara.exe_secure("test_enc.db")
        db.set(
            "test_key",
            'test_data:"ði ıntəˈnæʃənəl fəˈnɛtık əsoʊsiˈeıʃn Y [ˈʏpsilɔn], Yen [jɛn], Yoga [ˈjoːgɑ]"',
        )
        db.commit()
        db_load = elara.exe_secure("test_enc.db")
        recov_data = db_load.get("test_key")
        self.assertEqual(
            recov_data,
            'test_data:"ði ıntəˈnæʃənəl fəˈnɛtık əsoʊsiˈeıʃn Y [ˈʏpsilɔn], Yen [jɛn], Yoga [ˈjoːgɑ]"',
        )

        # cleanup database files
        os.remove("test_enc.db")
        os.remove("edb.key")
