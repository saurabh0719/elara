# Add tests here 

import unittest
import elara

class RunTests(unittest.TestCase):
    def setUp(self):
        self.db = elara.exe('test.db', False)

    def test_exe(self):
        res = elara.exe('test.db', False)
        assert res is not None

    def test_get(self):
        self.db.db['key'] = "test"
        res = self.db.db['key']
        self.assertEqual(res, 'test')
    
    def test_set(self):
        self.db.set('key', 'test')
        self.assertEqual(self.db.get('key'), 'test')

    def test_rem(self):
        self.db.set('key', 'test')
        assert 'key' in self.db.db
        self.db.rem('key')
        assert 'key' not in self.db.db

    def test_clear(self):
        self.db.set('key', 'test')
        self.assertEqual(self.db.clear(), True)
        self.assertEqual(self.db.db, {})
        
    def test_cull(self):
        self.db.set('one', 1)
        self.db.set('two', 2)
        self.db.set('three', 3)
        self.db.set('four', 4)
        self.db.cull(25)
        self.assertEqual(len(self.db.retmem()), 3)
        self.db.cull(100)
        self.assertEqual(len(self.db.retmem()), 0)
        self.assertEqual(self.db.cull(-1), False)
        self.assertEqual(self.db.cull(101), False)