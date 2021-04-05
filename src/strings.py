# Add String specific functions

def SETNX(self, key, data):
    if not self.EXISTS(key):
        self.SET(key, data)
    return True

def APPEND(self, key, data):
    value = self.db[key]
    self.db[key] = value + data
    self._dumpJSON()
    return True

def EXISTS(self, key):
    return key in self.db

def GETSET(self, key, data):
    old_data = self.db[key]
    self.SET(key, data)
    return old_data

def MSET(self, dict):
    for key in dict:
        self.SET(key, dict[key])
    return True

def MSETNX(self, dict):
    for key in dict:
        if not self.EXISTS(key):
            self.SET(key, dict[key])
    return True  

def SLEN(self, key):
    if self.EXISTS(key):
        return len(self.db[key])
    return -1
