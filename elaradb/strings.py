# Add String specific functions

def setnx(self, key, data):
    if not self.exists(key):
        self.set(key, data)
    return True

def append(self, key, data):
    value = self.db[key]
    self.db[key] = value + data
    self._autocommit()
    return True

def getset(self, key, data):
    old_data = self.db[key]
    self.set(key, data)
    return old_data

def mget(self, keys):
    result = []
    for key in keys:
        if self.exists(key):
            result.append(self.get(key))
    return result

def mset(self, dict):
    for key in dict:
        self.set(key, dict[key])
    return True

def msetnx(self, dict):
    for key in dict:
        if not self.exists(key):
            self.set(key, dict[key])
    return True  

def slen(self, key):
    if self.exists(key):
        return len(self.db[key])
    return -1
