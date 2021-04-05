"""
BSD 3-Clause License

Copyright (c) 2021, Saurabh Pujari
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from cryptography.fernet import Fernet
import json
import base64
import os

class Util:
    @staticmethod
    def readJSON(obj):
        try:
            curr_db = json.load(open(obj.path, 'rb'))
        except Exception:
            print("Read JSON error")
        return curr_db

    @staticmethod
    def storeJSON(obj):
        try:
            json.dump(obj.db, open(obj.path, 'wt'))
        except Exception:
            print("Store JSON error")
    
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
    def KEYGEN(path):
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

        

