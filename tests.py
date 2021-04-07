# Add tests here 

import unittest
import elaradb

class RunTests(unittest.TestCase):
    def setUp(self):
        self.db = elaradb.exe('test.db', False)
        
    def test_exe(self):
        res = elaradb.exe('test.db', False)
        assert res is not None