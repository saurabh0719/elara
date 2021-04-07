from .elara import Elara
from cryptography.fernet import Fernet
from .elarautil import Util

def exe(path, commitdb=False):
    return Elara(path, commitdb)

def exe_secure(path, commitdb=False, key_path='edb.key'):
    Util.loadkey(key_path)
    return Elara(path, commitdb, key_path)
