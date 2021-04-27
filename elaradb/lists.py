# Add list specific functions

def lnew(self, key):
    if isinstance(key, str):
        self.db[key] = []
        self._autocommit()
        return True
    else:
        raise Exception

def ladd(self, key, value):
    if self.exists(key):
        self.db[key].append(value)
        self._autocommit()
        return True
    else:
        return False

def lextend(self, key, data):
    if self.exists(key):
        self.db[key].extend(data)
        self._autocommit()
        return True
    else: 
        return False

def lindex(self, key, index):
    if self.exists(key) and len(self.db[key])>index:
        return self.db[key][index]
    else:
        return False

def lrange(self, key, start=None, end=None):
    return self.db[key][start:end]

def lrem(self, key, value):
    if self.exists(key) and len(self.db[key])>0:
        self.db[key].remove(value)
        self._autocommit()
        return True
    else: 
        return False

def lpop(self, key, pos=-1):
    len = self.llen(key)
    if self.exists(key) and pos<len:
        if pos<-1: 
            return False
        else:
            value = self.db[key][pos]
            del self.db[key][pos]
            self._autocommit()
            return value
    else:                  
        return False

def llen(self, key):
    if self.exists(key):
        return len(self.db[key])
    else: 
        return -1

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