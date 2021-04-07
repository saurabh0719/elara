# Hash table operations

def hnew(self, key):
    if isinstance(key, str):
        self.db[key] = {}
        self._autocommit()
        return True
    else:
        raise Exception

def hadd(self, key, dict_key, value):
    self.db[key][dict_key] = value
    self._autocommit()
    return True

def haddt(self, key, tuple):
    self.db[key][tuple[0]] = tuple[1]
    self._autocommit()
    return True

def hget(self, key, dict_key):
    return self.db[key][dict_key]

def hpop(self, key, dict_key):
    value = self.db[key][dict_key]
    del self.db[key][dict_key]
    self._autocommit()
    return value

def hkeys(self, key):
    return self.db[key].keys()

def hvals(self, key):
    return self.db[key].values()

def hexists(self, key, dict_key):
    return dict_key in self.db[key]

def hmerge(self, key1, key2):
    first = self.db[key1]
    second = self.db[key2]
    first.update(second)
    self._autocommit()
    return True