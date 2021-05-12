"""
Copyright (c) 2021, Saurabh Pujari
All rights reserved.

This source code is licensed under the BSD-style license found in the LICENSE file in the root directory of this source tree.
"""

from cryptography.fernet import Fernet
import json
import base64
import os
from .exceptions import FileAccessError, FileKeyError

class Util:
    @staticmethod
    def readJSON(obj):
        try:
            curr_db = json.load(open(obj.path, 'rb'))
        except Exception:
            # print("Read JSON error. File might be encrypted. Run in secure mode.")
            raise FileAccessError("Read JSON error. File might be encrypted. Run in secure mode with key path.")
        return curr_db

    @staticmethod
    def storeJSON(obj):
        try:
            json.dump(obj.db, open(obj.path, 'wt'), indent=4)
        except Exception:
            raise FileAccessError("Store JSON error. File might be encrypted. Run in secure mode with key path.")
    
    @staticmethod
    def readAndDecrypt(obj):
        if obj.key:
            fernet = Fernet(obj.key)
            encrypted_data = None
            try:
                with open(obj.path, 'rb') as file:
                    encrypted_data = file.read()
            except Exception:
                raise FileAccessError("File open & read error")
            decrypted_data = fernet.decrypt(encrypted_data)
            return json.loads(decrypted_data.decode("utf-8"))
        else:
            return None

    @staticmethod
    def encryptAndStore(obj):
        if obj.key:
            fernet = Fernet(obj.key)
            db_snapshot = json.dumps(obj.db)
            db_byte = db_snapshot.encode("utf-8")
            encrypted_data = fernet.encrypt(db_byte)
            try:
                with open(obj.path, 'wb') as file:
                    file.write(encrypted_data)
                    return True
            except Exception:
                raise FileAccessError("File open & write error")
        else:
            return False

    @staticmethod
    def keygen(path):
        try:
            key = Fernet.generate_key()
        except Exception:
            raise FileKeyError("Key generation error")
        try:
            with open(path, 'wb') as file:
                file.write(key)
            file.close()
            return True
        except Exception:
            raise FileAccessError("File open & write error")


    @staticmethod
    def loadkey(path):
        key_path = os.path.expanduser(path)
        # print(key_path)

        if os.path.exists(key_path):
            if os.stat(key_path).st_size == 0: 
                Util.keygen(key_path)
                # else: key exists in file; use that
        else:
            # create file and store keygen
            Util.keygen(key_path)

    @staticmethod
    def readkey(path):
        key_path = os.path.expanduser(path)
        if os.path.exists(key_path):
            file = open(key_path, 'rb')
            key = file.read()
            file.close()
            return key
        else:
            key = None
            return key
