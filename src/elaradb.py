from elara import Elara

def load(path):
    '''Return a pickledb object. location is the path to the json file.'''
    return Elara(path)