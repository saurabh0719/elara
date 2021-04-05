import os
import json

class Elara(object):

    from strings import (SETNX, APPEND, EXISTS, GETSET, MSET, MSETNX, SLEN)

    from lists import (LNEW, LADD, LEXTEND, LINDEX, LRANGE,
                       LDEL, LPOP, LLEN, LAPPEND, LEXISTS, LINSERT)
                       
    from hashtables import (HNEW, HADD, HADDT, HGET, HPOP, HKEYS, HVALS, HEXISTS, HMERGE)

    def __init__(self, path):
        '''Creates a database object and loads the data from the location path.
        If the file does not exist it will be created on the first update.'''
        new_path = os.path.expanduser(path)
        self.path = new_path
        if os.path.exists(path):
            self._loadJSON()
        else:
            self.db = {}

    def _loadJSON(self):
        self.db = json.load(open(self.path, 'rb'))

    def _dumpJSON(self):
        json.dump(self.db, open(self.path, 'wt'))
    
    def SAVE(self):
        self._dumpJSON()
        return True
    
    def SET(self, key, value):
        self.db[key] = value
        self._dumpJSON()
        return True
    
    def GET(self, key):
        try:
            return self.db[key]
        except KeyError:
            return None
    
    def DEL(self, key):
        del self.db[key]
        self._dumpJSON()
        return True
    
    def CLEAR(self):
        self.db = {}
        self._dumpJSON()
        return True