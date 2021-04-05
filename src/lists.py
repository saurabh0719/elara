# Add list specific functions

def LNEW(self, key):
    self.db[key] = []
    self._dumpJSON()
    return True

def LADD(self, key, value):
    self.db[key].append(value)
    self._dumpJSON()
    return True

def LEXTEND(self, key, seq):
    self.db[key].extend(seq)
    self._dumpJSON()
    return True

def LINDEX(self, key, index):
    return self.db[key][index]

def LRANGE(self, key, start=None, end=None):
    return self.db[key][start:end]

def LDEL(self, key, value):
    self.db[key].remove(value)
    self._dumpJSON()
    return True

def LPOP(self, key, pos):
    value = self.db[key][pos]
    del self.db[key][pos]
    self._dumpJSON()
    return value

def LLEN(self, key):
    return len(self.db[key])

def LAPPEND(self, key, pos, more):
    tmp = self.db[key][pos]
    self.db[key][pos] = tmp + more
    self._dump()
    return True

def LEXISTS(self, key, value):
    # modify and return index
    return value in self.db[key]

def LINSERT(self, key, value, index):
    pass