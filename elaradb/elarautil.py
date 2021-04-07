from cryptography.fernet import Fernet
import json
import base64
import os
from .exceptions import SomeRandomError

class Util:
    @staticmethod
    def readJSON(obj):
        try:
            curr_db = json.load(open(obj.path, 'rb'))
        except Exception:
            # print("Read JSON error. File might be encrypted. Run in secure mode.")
            raise SomeRandomError("Read JSON error. File might be encrypted. Run in secure mode.")
        return curr_db

    @staticmethod
    def storeJSON(obj):
        try:
            json.dump(obj.db, open(obj.path, 'wt'), indent=4)
        except Exception:
            print("Store JSON error. File might be encrypted. Run in secure mode with key path.")
    
    @staticmethod
    def readAndDecrypt(obj):
        if obj.key:
            fernet = Fernet(obj.key)
            encrypted_data=""
            try:
                with open(obj.path, 'rb') as file:
                    encrypted_data = file.read()
            except Exception:
                print("File open & read error")
            decrypted_data = fernet.decrypt(encrypted_data)
            data_bytes = base64.b64decode(decrypted_data)
            data_ascii = data_bytes.decode('ascii')
            data_ascii = data_ascii.replace("'", "\"")
            curr_db = json.loads(data_ascii)
            return curr_db
        else:
            return None

    @staticmethod
    def encryptAndStore(obj):
        if obj.key:
            fernet = Fernet(obj.key)
            db_curr = str(obj.db)
            db_ascii = db_curr.encode('ascii')
            db_byte = base64.b64encode(db_ascii)
            encrypted_data = fernet.encrypt(db_byte)
            try:
                with open(obj.path, 'wb') as file:
                    file.write(encrypted_data)
                    return True
            except Exception:
                print("File open & write error")
        else:
            return False

    @staticmethod
    def keygen(path):
        key_path = os.path.expanduser(path)
        # print(key_path)
        key=""
        if os.path.exists(key_path):
            if os.stat(key_path).st_size == 0: 
                try:
                    key = Fernet.generate_key()
                except Exception:
                    print("Key generation error")
                try:
                    with open(key_path, 'wb') as file:
                        file.write(key)
                    file.close()
                    return True
                except Exception:
                    print("File open & write error")
                # else: key exists in file; use that
        else:
            # create file and store keygen
            try:
                key = Fernet.generate_key()
            except Exception:
                print("Key generation error")
            try:
                with open(key_path, 'wb') as file:
                    file.write(key)
                file.close()
                return True
            except Exception:
                print("File open & write error")
