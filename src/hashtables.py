# Add hash/Dictionary specific functions

def HNEW(self, key):
    self.db[key] = {}
    self._autodumpdb()
    return True

def HADD(self, key, dict_key, value):
    self.db[key][dict_key] = value
    self._dumpJSON()
    return True

def HADDT(self, key, tuple):
    self.db[key][tuple[0]] = tuple[1]
    self._dumpJSON()
    return True

def HGET(self, key, dict_key):
    return self.db[key][dict_key]

def HPOP(self, key, dict_key):
    value = self.db[key][dict_key]
    del self.db[key][dict_key]
    self._dumpJSON()
    return value

def HKEYS(self, key):
    return self.db[key].keys()

def HVALS(self, key):
    return self.db[key].values()

def HEXISTS(self, key, dict_key):
    return dict_key in self.db[key]

def HMERGE(self, key1, key2):
    first = self.db[key1]
    second = self.db[key2]
    first.update(second)
    self._dumpJSON()
    return True