# shared operations
from cryptography.fernet import Fernet
from .elarautil import Util
import json
import os

def retdb(self):
    if self.key:
        return Util.readAndDecrypt(self)
    else:
        return Util.readJSON(self)

def retmem(self):
    return self.db

def retkey(self):
    return self.key

def commit(self):
    self._dump()

def exists(self, key):
    return key in self.db
    
def exportdb(self, export_path, sort=True):
    db = self.retdb()
    new_export_path = os.path.expanduser(export_path)
    try:
        json.dump(db, open(new_export_path, 'wt'), indent=4, sort_keys=sort)
    except Exception:
        print("Store JSON error. File path might be wrong")

def exportmem(self, export_path, sort=True):
    db = self.retmem()
    new_export_path = os.path.expanduser(export_path)
    try:
        json.dump(db, open(new_export_path, 'wt'), indent=4, sort_keys=sort)
    except Exception:
        print("Store JSON error. File path might be wrong")

def exportkeys(self, export_path, keys = [], sort=True):
    db = {}
    for key in keys:
        if isinstance(key, str) and self.exists(key):
            db[key] = self.get(key)

    new_export_path = os.path.expanduser(export_path)
    try:
        json.dump(db, open(new_export_path, 'wt'), indent=4, sort_keys=sort)
    except Exception:
        print("Store JSON error. File path might be wrong")


# Incomplete function
def updatekey(self, key_path=None):
    if self.key:
        new_key_path = os.path.expanduser(key_path)
        self.db = self.retdb()
        if os.path.exists(new_key_path):
            if os.stat(new_key_path).st_size == 0: 
                Util.keygen(new_key_path)
            else:
                # os.remove(new_key_path)
                f = open(new_key_path, 'r+')
                f.truncate(0)
                f.close()
                Util.keygen(new_key_path)

        else:
            Util.keygen(new_key_path)

        #clear db file and encrypt contents with new key
        f = open(self.path, 'r+')
        f.truncate(0)
        f.close 
        self.key = Util.readkey(new_key_path)
        Util.encryptAndStore(self)
        
    else:
        raise Exception

    # write function to check if db file exists/ there is data present in it