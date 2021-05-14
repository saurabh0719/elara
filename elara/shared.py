"""
Copyright (c) 2021, Saurabh Pujari
All rights reserved.

This source code is licensed under the BSD-style license found in the LICENSE file in the root directory of this source tree.
"""

# shared operations
from cryptography.fernet import Fernet
from .elarautil import Util
import json
import os
from .exceptions import FileAccessError, FileKeyError


def retdb(self):
    if self.key:
        return Util.read_and_decrypt(self)
    else:
        return Util.read_plain_db(self)


def retmem(self):
    return self.db


def retkey(self):
    return self.key


def commit(self):
    self._dump()


def exportdb(self, export_path, sort=True):
    db = self.retdb()
    new_export_path = os.path.expanduser(export_path)
    try:
        json.dump(db, open(new_export_path, "wt"), indent=4, sort_keys=sort)
    except Exception:
        raise FileAccessError("Store JSON error. File path might be wrong")


def exportmem(self, export_path, sort=True):
    db = self.retmem()
    new_export_path = os.path.expanduser(export_path)
    try:
        json.dump(db, open(new_export_path, "wt"), indent=4, sort_keys=sort)
    except Exception:
        raise FileAccessError("Store JSON error. File path might be wrong")


def exportkeys(self, export_path, keys=[], sort=True):
    db = {}
    for key in keys:
        if isinstance(key, str) and self.exists(key):
            db[key] = self.get(key)

    new_export_path = os.path.expanduser(export_path)
    try:
        json.dump(db, open(new_export_path, "wt"), indent=4, sort_keys=sort)
    except Exception:
        raise FileAccessError("Store JSON error. File path might be wrong")


def securedb(self, key_path=None):
    if key_path is None:
        raise FileAccessError("Please specify a valid key path")
    elif self.key:
        self.updatekey(self, key_path)
    else:
        new_key_path = os.path.expanduser(key_path)
        self.db = self.retdb()  # Store the current contents

        if os.path.exists(new_key_path):
            if os.stat(new_key_path).st_size == 0:
                Util.keygen(new_key_path)
            else:
                # os.remove(new_key_path)
                f = open(new_key_path, "r+")
                f.truncate(0)
                f.close()
                Util.keygen(new_key_path)
        else:
            Util.keygen(new_key_path)

        self.key = Util.readkey(new_key_path)
        Util.encrypt_and_store(self)
        return True


# Incomplete function
def updatekey(self, key_path=None):
    if key_path is None:
        raise FileAccessError("Please specify a valid key path")
    elif self.key:
        new_key_path = os.path.expanduser(key_path)
        self.db = self.retdb()
        if os.path.exists(new_key_path):
            if os.stat(new_key_path).st_size == 0:
                Util.keygen(new_key_path)
            else:
                # os.remove(new_key_path)
                f = open(new_key_path, "r+")
                f.truncate(0)
                f.close()
                Util.keygen(new_key_path)

        else:
            Util.keygen(new_key_path)

        # clear db file and encrypt contents with new key
        f = open(self.path, "r+")
        f.truncate(0)
        f.close
        self.key = Util.readkey(new_key_path)
        Util.encrypt_and_store(self)

    else:
        raise FileKeyError("Update key Failed")
