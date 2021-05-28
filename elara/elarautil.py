"""
Copyright (c) 2021, Saurabh Pujari
All rights reserved.

This source code is licensed under the BSD-style license found in the LICENSE file in the root directory of this source tree.
"""
import multiprocessing
import os
from typing import Dict
from zlib import crc32

import msgpack
import safer
from cryptography.fernet import Fernet

from .exceptions import (
    FileAccessError,
    FileKeyError,
    LoadChecksumError,
    LoadIncompatibleDB,
)


class Util:
    @staticmethod
    def check_mag(mag):
        return mag == b"ELDB"

    @staticmethod
    def check_encrypted(version):
        # if msb of version number is set the db is encrypted
        return (version & (1 << 15)) != 0

    @staticmethod
    def read_plain_db(obj) -> Dict:
        with safer.open(obj.path, "rb") as fctx:
            if not Util.check_mag(fctx.read(4)):
                raise FileAccessError("File magic number not known")
            version = int.from_bytes(fctx.read(2), "little", signed=False)
            # check for encryption before trying anything
            if Util.check_encrypted(version):
                raise FileAccessError("This file is encrypted, run in secure mode")
            checksum = int.from_bytes(fctx.read(4), "little", signed=False)
            data = fctx.read()
            calculated_checksum = crc32(data)
            if calculated_checksum != checksum:
                raise LoadChecksumError(
                    f"calculated checksum: {calculated_checksum} is different from stored checksum {checksum}"
                )
            elif version != obj.db_format_version:
                raise LoadIncompatibleDB(
                    f"db format version {version} is incompatible with {obj.db_format_version}"
                )
            try:
                curr_db = msgpack.unpackb(data)
            except FileNotFoundError:
                raise FileAccessError("File not found")
            return curr_db

    @staticmethod
    def store_plain_db(obj, lock):
        data = msgpack.packb(obj.db)
        buffer = b"ELDB"
        buffer += obj.db_format_version.to_bytes(2, "little")
        buffer += (crc32(data)).to_bytes(4, "little")
        buffer += data
        try:
            lock.acquire()
            with safer.open(obj.path, "wb") as file:
                file.write(buffer)
                lock.release()
                return True

        except:
            raise FileAccessError("File already exists")

    @staticmethod
    def read_and_decrypt(obj):
        if obj.key:
            fernet = Fernet(obj.key)
            try:
                with safer.open(obj.path, "rb") as fctx:
                    if not Util.check_mag(fctx.read(4)):
                        raise FileAccessError("File magic number not known")
                    version = int.from_bytes(fctx.read(2), "little")
                    if not Util.check_encrypted(version):
                        raise FileAccessError(
                            "File is marked not encrypted, you might have a corrupt db"
                        )
                    checksum = int.from_bytes(fctx.read(4), "little")
                    encrypted_data = fctx.read()
                    calculated_checksum = crc32(encrypted_data)
                    if calculated_checksum != checksum:
                        raise LoadChecksumError(
                            f"calculated checksum: {calculated_checksum} is different from stored checksum {checksum}"
                        )
            except FileNotFoundError:
                raise FileAccessError("File open & read error")
            decrypted_data = fernet.decrypt(encrypted_data)
            return msgpack.unpackb(decrypted_data)
        else:
            return None

    @staticmethod
    def encrypt_and_store(obj, lock):
        # pass lock maybe.
        if obj.key:
            fernet = Fernet(obj.key)
            db_snapshot = msgpack.packb(obj.db)
            buffer = b"ELDB"
            # set version msb
            buffer += (obj.db_format_version | 1 << 15).to_bytes(2, "little")
            encrypted_data = fernet.encrypt(db_snapshot)
            buffer += crc32(encrypted_data).to_bytes(4, "little")
            buffer += encrypted_data
            try:

                lock.acquire()
                with safer.open(obj.path, "wb") as file:
                    file.write(buffer)
                    lock.release()
                    return True

            except FileExistsError:
                raise FileAccessError("File already exists")
        else:
            return False

    @staticmethod
    def keygen(path):
        try:
            key = Fernet.generate_key()
        except Exception:
            raise FileKeyError("Key generation error")
        try:
            with safer.open(path, "wb") as file:
                file.write(key)
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
            file = safer.open(key_path, "rb")
            key = file.read()
            file.close()
            return key
        else:
            key = None
            return key
