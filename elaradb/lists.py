# Add list specific functions

def lnew(self, key):
    if isinstance(key, str):
        self.db[key] = []
        self._autocommit()
        return True
    else:
        raise Exception

def ladd(self, key, value):
    self.db[key].append(value)
    self._autocommit()
    return True

def lextend(self, key, data):
    self.db[key].extend(data)
    self._autocommit()
    return True

def lindex(self, key, index):
    return self.db[key][index]

def lrange(self, key, start=None, end=None):
    return self.db[key][start:end]

def lrem(self, key, value):
    self.db[key].remove(value)
    self._autocommit()
    return True

def lpop(self, key, pos):
    value = self.db[key][pos]
    del self.db[key][pos]
    self._autocommit()
    return value

def llen(self, key):
    return len(self.db[key])

def lappend(self, key, pos, more):
    tmp = self.db[key][pos]
    self.db[key][pos] = tmp + more
    self._autocommit()
    return True

def lexists(self, key, value):
    # modify and return index
    return value in self.db[key]

def linsert(self, key, value, index):
    pass