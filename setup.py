"""
Elara
--------
Elara DB is an easy to use key-value storage for your python projects!

Installation :
```````````````````
::

    $ pip install elara   
    
Key Features :
```````````````
* Offers two modes of execution - normal and secure - exe_secure() generates a key file and encrypts the key-value storage for additional security.
* Perform various operations on strings, lists and dictionaries.
* Choose between manual commits after performing operations in-memory or automatically commit every change into the storage.
* Includes methods to export certain keys or the entire storage.
* Based on python's in-built json module for easy manipulation and access.
* Takes inspiration from pickleDB and Redis.
    
Links
`````
* `Documentation <https://github.com/saurabh0719/elara#readme>`_
* `pypi <https://pypi.org/project/elara/>`_
* `Github repository <https://github.com/saurabh0719/elara>`_

"""

from distutils.core import setup
    
setup(
  name = 'elara',         
  packages = ['elara'],   
  version = '0.1.3',      
  license='three-clause BSD',        
  description = 'Elara DB is an easy to use key-value storage for your python projects!',   
  long_description = __doc__,
  author = 'Saurabh Pujari',                   
  author_email = 'saurabhpuj99@gmail.com',      
  url = 'https://github.com/saurabh0719/elara',  
  keywords = [
    'database',
    'key-value',
    'storage',
    'file storage',
    'json storage',
    'json database'
    'key-value database'  
    ],   # Keywords that define your package best
  install_requires=[
    'cryptography'
    ],
  classifiers=[
    'Development Status :: 4 - Beta',      
    'Intended Audience :: Developers',      
    'Topic :: Database',
    'License :: OSI Approved :: BSD License',   
    'Programming Language :: Python'
  ],
)