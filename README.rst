Elara 
-----

Elara DB is an easy to use, lightweight key-value database written for python that can also be used as a fast in-memory cache for JSON-serializable data. Includes various methods and features to manipulate data structures in-memory, protect database files and export data.

View the `Github repository <https://github.com/saurabh0719/elara>`__ and the `official docs <https://github.com/saurabh0719/elara#readme>`__.

.. code:: sh

    $ pip install elara


Go through the release notes for details on upgrades as breaking changes might happen between version upgrades while Elara is in beta.

Elara DB has official support for python 3.6, 3.7, 3.8 and 3.9.

Key Features
------------

-  Offers three modes of execution - normal, cache and secure - secure mode generates a key file and encrypts the database for additional security.
-  Manipulate data structures such as strings, lists and dictionaries.
-  Fast and flexible in-memory LRUcaching mechanism.
-  Supports keys of any type, not just strings!
-  Choose between manual commits after performing operations in-memory
   or automatically commit every change into the storage.
-  Includes methods to export certain keys from the database or the
   entire storage.
-  Incorporates checksums to verify database file integrity.


Installation
------------

From `pypi <https://pypi.org/project/elara/>`__ :

.. code:: sh

    $ pip install elara

OR,

Clone the repository and install the dependencies :

.. code:: sh

    $ pip install -r requirements.py
    $ python -m unittest -v     # Run tests

License
-------

::

    Copyright (c) 2021, Saurabh Pujari
    All rights reserved.

    This source code is licensed under the BSD-style license found in the LICENSE file in the root directory of this source tree.

Fundamentals
------------

Basic usage :
~~~~~~~~~~~~~

.. code:: python

   import elara as elara

   db = elara.exe("new.db")

   db.set("name", "Elara")

   print(db.get("name"))
   # Elara

You can choose between normally transacting data from the database 
or you can protect your database with a key.

.. code:: python

    import elara

    # exe_secure() encrypts the db file
    db = elara.exe_secure("new.db", True, "newdb.key")

    # OR
    # db = elara.exe_secure(path="path/new.db", commitdb=True, key_path="path/edb.key")

    db.set("name", "Elara")

    print(db.get("name"))
    # Elara

-  ``exe_secure(path, commitdb=False, key_path="edb.key")`` - Loads the
   contents of the encrypted database (using the key file) into the
   program memory or generates a new key file (default - `edb.key`) if it doesn't exist
   in the given path and it encrypts/decrypts the
   database file. 

Using ``exe_secure()`` without a key file or without the correct key
file corresponding to the database will result in errors. Database files are verified with checksums to maintain integrity.
Key files and DB files can be included inside the ``.gitignore`` to ensure they're not
pushed into an upstream repository.

-  ``commitdb`` - this argument defaults to ``False`` ie. you will
   have to manually call the ``commit()`` method to write the in-memory
   changes into the database. If set to ``True``, changes will be
   written into the file after every operation.

.. code:: python

    import elara

    db = elara.exe_secure(path="path/new.db",  key_path="path/edb.key") # commit=False  

    db.set("num", 20)

    print(db.get("num"))
    # 20

    db.commit() # Writes in-memory changes into the file

-  ``exe(path, commitdb=False)`` - Loads the contents of the
   database into the program memory or generates a new database file if
   it doesn't exist in the given path. 
   The database file is NOT protected and can be accessed without a key.

.. code:: python

    import elara as elara

    db = elara.exe("new.db", True)

    db.set("name", "Elara")

    print(db.get("name"))
    # Elara

All the following operations are methods that can be applied to the
instance returned from ``exe()`` or ``exe_secure()``. These operations
manipulate/analyse data in-memory after the Data is loaded from the
file. Set the ``commit`` argument to ``True`` else manually use the
``commit()`` method to sync in-memory data with the database file.

-  ``get(key)`` - returns the corresponding value from the db or
   ``None``
-  ``set(key, value)`` - returns ``True`` or an Exception. The ``key``
   can be any data type that is supported by python dictionaries (int, float, string etc.).
-  ``rem(key)`` - deletes the key-value pair if it exists.
-  ``remkeys(keys=[])`` - deletes all the key-value pairs from the list of keys given, if the key exists.
-  ``clear()`` - clears the database data currently stored in-memory.
-  ``exists(key)`` - returns ``True`` if the key exists.
-  ``commit()`` - write in-memory changes into the database file.
-  ``getset(key, value)`` - Sets the new value and returns the old value
   for that key or returns ``False``.
-  ``getkeys()`` - returns the list of keys in the database with. The
   list is ordered with the ``most recently accessed`` keys starting
   from index 0.
-  ``getmatch(match)`` - Takes the ``match`` argument and returns a 
   Dictionary of key-value pairs of which the keys contain ``match`` as a sub string.
-  ``numkeys()`` - returns the number of keys in the database.
-  ``retkey()`` - returns the Key used to encrypt/decrypt the db file;
   returns ``None`` if the file is unprotected.
-  ``retmem()`` - returns all the in-memory db contents.
-  ``retdb()`` - returns all the db file contents.

.. code:: python

    import elara

    db = elara.exe("new.db")

    db.set("num1", 20)

    # ("num1", 20) is written into the file db
    db.commit()

    db.set("num2", 30)

    print(db.retmem())
    # {'num1': 20, 'num2': 30}

    print(db.retdb())
    # {'num1': 20}

Note - ``retmem()`` and ``retdb()`` will return the same value if
``commit`` is set to ``True`` or if the ``commit()`` method is used
before calling ``retdb()``

Elara adds some syntax sugar for get(), set() and rem() :

.. code:: python

   import elara

   db = elara.exe("new.db")

   db["key"] = "value"

   print(db["key"])
   # value

   del self.db["key"]

   print(db.retmem())
   # {}

Cache:
~~~~~~

Elara can also be used as a fast in-memory cache. 

-  ``exe_cache(path, cache_param=None, commit=False)`` - This function creates an instance with the settings defined in ``cache_param``. 
   Here ``commit`` defaults to ``False`` to allow for in-memory manipulation.
   
   -  ``cache_param`` - This argument is a dictionary that can define of 3 `optional` parameters. 

      -  ``max_age`` - This is the default amount of time in ``seconds`` that any key stored (eg. using `set()`) into the cache will last for before being evicted. 
         Defaults to ``None`` which indicates it will stay in memory for as long as the instance is running.
      -  ``max_size`` - This is the maximum number of keys that will be stored in the cache. For every key addition request after the ``max_size`` limit has been reached, an automatic ``cull()`` is called to evict some keys based on ``cull_freq``. 
         Defaults to positive infinity as limited by the device.
      -  ``cull_freq`` - This is the default amount of keys, in percentage, that will be evicted based on the LRU eviction strategy when the cache reaches its ``max_size``. 0 <= ``cull_freq`` <=100. 
         Defaults to ``20`` ie. 20% of all keys will be deleted based on the LRU eviction strategy.

The LRU eviction searches for, and deletes, expired keys lazily after every function call.

Note - In ``exe_cache``, the ``path`` parameter is a required argument in case you need to commit your cache contents into the database. 

-  ``set(key, value, max_age=None)`` - The ``set()`` function takes another argument, ``max_age``, that is set to ``None`` by default ie. the key-value pair will follow the default ``max_age`` set in ``cache_param`` OR they stay never get evicted if ``cache_param`` is not defined. The ``max_age`` param in ``set()`` allows for more granular control over cache item expiry. 
   ``max_age`` should be an integer greater than 0. ``max_age = "i"`` indicates the item will not be removed from memory (overrides default ``max_age`` or ``max_age`` defined in ``cache_param``)
  
Similarly, ``lnew(key, max_age=None)``, ``hnew(key, max_age=None)`` (read the API reference) and ``getset(key, value, max_age=None)``, all accept the optional ``max_age`` argument.
  

.. code:: python

   import elara 

   cache_param = {
       "max_age": 900,
       "max_size": 4,
       "cull_freq": 25
   }

   cache = elara.exe_cache(path="new.db", cache_param=cache_param)

   # OR
   # cache = elara.exe_cache("new.db", cache_param)

   cache.set("key1", "This one will be evicted in 900 seconds")
   cache.set("key2", "This one will not be evicted", "i") # 'i' signifies it will never be evicted 
   cache.set("key3", "This one will be evicted in 100 seconds", 50)

   print(cache.getkeys())
   # ["key3", "key2", "key1"]

   time.sleep(50)

   print(cache.getkeys())
   # ["key2", "key1"]

   cache.set("key3", 5)
   cache.set("key4", 10)

   print(cache.getkeys())
   # ["key4", "key3", "key2", "key1"]

   cache.set("key1", 7, "i")    # overwrite "key1" to never expire

   print(cache.getkeys())
   # ["key1", "key4", "key3", "key2"]

   print(cache.get("key1"))
   # 7

   cache.set("key5", 20)   # Automatic culling when max_size is reached

   print(cache.getkeys())
   # ["key5", "key1", "key4", "key3"]

Elara also allows for manual culling of cached items :

-  ``cull(percentage)`` - ``percentage`` (0 <= percentage <= 100)
   defines the percentage of Key-Value pairs to be deleted, with the
   ``Least recently accessed`` keys being deleted first. Elara maintains a
   simple LRU list to track key access.

.. code:: python

   import elara

   """
   Without the cache_param argument, all defauls will be set
   
   Passing any one of the values is also valid as mentioned above 
   cache = elara.exe_cache("new.db", {"max_size": 100}))
   
   """
   
   cache = elara.exe_cache("new.db")
   
   cache.set("num1", 10)
   cache.set("num2", 20)
   cache.set("num3", 30)
   cache.set("num4", 40)
   
   if cache.exists("num1"):
       print(cache.get("num1"))
       # 10 
       
   print(cache.retmem())
   # {'num1': 10, 'num2': 20, 'num3': 30, 'num4': 40}
   
   # most recently accessed keys come first
   print(cache.getkeys())
   # ['num1', 'num4', 'num3', 'num2']
   
   # delete 25% of the stale keys (follows LRU)
   cache.cull(25) 
   
   # most recently accessed keys come first
   print(cache.getkeys())
   # ['num1', 'num4', 'num3']


-  ``ttl(key)`` - returns the time to live of the key as a ``datetime.timedelta()`` object or returns ``None`` if it does not have an expiration value. 
   Returns ``False`` if the key is missing. 
-  ``ttls(key)`` - returns the time to live of the key in ``seconds``. Returns ``False`` if the key is missing.
-  ``persist(key)`` - sets the expiry value of the key to ``None``, hence persisting it. Returns ``False`` if the key is missing.

Serialization and Storage :
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Elara supports basic python datatypes (`int`, `str`, `dict`, `list` etc.).
However, objects (simple and complex) can be stored and retrieved using `get`, `set` and other functions that apply to them
as long as they are ``in-memory`` and ``not persisted in the file``, as that would lead to serialization errors. 

.. code:: python

   import elara

   cache = elara.exe("new.db") # commit = False by default

   class MyObj():
       def __init__(self, num):
           self.num = num

   obj = MyObj(19)

   cache.set("obj", obj)

   print(cache.get("obj").num)
   # 19  

-  To persist a simple object as a dictionary, use the ``__dict__`` attribute.
-  Elara uses checksums and a file version flag to verify database file integrity.

All database writes are atomic (uses the safer library). Database writes are done in a separate thread along with a thread lock.

API reference
-------------

Strings :
~~~~~~~~~

-  ``mget(keys)`` - takes a list of keys as an argument and returns a
   list with all the corresponding values IF they exist; returns an
   empty list otherwise.
-  ``mset(dict)`` - takes a dictionary of key-value pairs as an argument
   and calls the ``set(key, value)`` method for each pair. Keys have to
   be a String.
-  ``setnx(key, value)`` - Sets the key-value if the key does not exist
   and returns ``True``; returns ``False`` otherwise.
-  ``msetnx(dict)`` - takes a dictionary of key-value pairs as an
   argument and calls the ``setnx(key, value)`` method for each pair.
   Keys have to be a string.
-  ``slen(key)`` - returns the length of the string value if the key
   exists; returns ``-1`` otherwise.
-  ``append(key, data)`` - Append the data (String) to an existing
   string value; returns ``False`` if it fails.

Lists :
~~~~~~~

-  ``lnew(key)`` - Initialises an empty list for the given key and
   returns ``True`` or an Exception; key can be any data type that is supported by python dictionaries (int, float, string etc.).
-  ``lpush(key, value)`` - Appends the given value to the list and
   returns ``True``; returns ``False`` if the key does not exist.
-  ``lpop(key)`` - Pops and returns the last element of the list if it
   exists; returns ``False`` otherwise. Index of the element can be
   passed to delete a specific element using ``lpop(key, pos)``. ``pos``
   defaults to ``-1`` (last element of the list).
-  ``lrem(key, value)`` - remove a value from the list. Returns ``True``
   on success and ``False`` otherwise.
-  ``llen(key)`` - returns length of the list if the key exists; returns
   ``-1`` otherwise.
-  ``lindex(key, index)`` - takes the index as an argument and returns
   the value if the key and list exist; returns ``False`` otherwise.
-  ``lrange(key, start, end)`` - takes ``start`` and ``end`` index as
   arguments and returns the list within the given range. Value at
   ``end`` not included. Returns empty list if start/end are invalid.
-  ``lextend(key, new_list)`` - Extend the list with ``new_list`` if the
   key exists. Returns ``True`` or ``False`` if the key does not exist.
-  ``lexists(key, value)`` - returns ``True`` if the value is present in
   the list; returns ``False`` otherwise.
-  ``lappend(key, pos, value)`` - appends ``value`` to the existing data
   at index ``pos`` using the ``+`` operator. Returns ``True`` or
   ``False``.

.. code:: python

    import elara

    db = elara.exe(path='new.db', commitdb=True)

    db.lnew('newlist')
    db.lpush('newlist', 3)
    db.lpush('newlist', 4)
    db.lpush('newlist', 5)

    print(db.lpop('newlist'))
    # 5

    print(db.lindex('newlist', 0))
    # 3

    new_list = [6, 7, 8, 9]
    db.lextend('newlist', new_list)
    print(db.get('newlist'))
    # [3, 4, 6, 7, 8, 9]

 

Hashtable/Dictionary :
~~~~~~~~~~~~~~~~~~~~~~

-  ``hnew(key)`` - Initialises an empty dictionary for the given key and
   returns ``True`` or an Exception; key can be any data type that is supported by python dictionaries (int, float, string etc.).
-  ``hadd(key, dict_key, value)`` - Assigns a value to a dictionary key
   and returns ``True``; returns ``False`` if the dictionary doesn't
   exist.
-  ``haddt(key, tuple)`` - Add a new key-value tuple into the
   dictionary. Returns ``True`` if the dictionary exists; returns
   ``False`` otherwise.
-  ``hget(key, dict_key)`` - Returns the value from the dictionary;
   returns ``False`` if the dictionary doesn't exist.
-  ``hpop(key, dict_key)`` - Deletes the given key-value pair from the
   dictionary and returns the deleted value; returns ``False`` if the
   dictionary doesn't exist.
-  ``hkeys(key)`` - returns all the Keys present in the dictionary.
-  ``hvals(key)`` - returns all the values present in the dictionary.
-  ``hmerge(key, dict)`` - updates (dict.update()) the dictionary
   pointed by the key with the new dictionary ``dict`` passed as an
   argument.

Update key and Secure DB :
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  ``updatekey(key_path)`` - This method works for instances produced by
   ``exe_secure()``. It updates the key in the key file path and
   re-encyrpts the database with the new key. If the file doesn't exist,
   the method generates a new file with a key and uses that to encrypt
   the database file.

.. code:: python

    import elara 

    # exe_secure() encrypts the db file
    db = elara.exe_secure("new.db", True, "newdb.key")
    db.set("name", "Elara")

    print(db.get("name"))
    # Elara

    db.updatekey('newkeypath.key')

    # Regular program flow doesn't get affected by key update
    print(db.get("name"))   
    # Elara

However, the next time you run the program, you have to pass the new
updated key (``newkeypath.key`` in this case) to avoid errors.

-  ``securedb(key_path)`` - Calls ``updatekey(key_path)`` for instances
   which are already protected with a key. For an unprotected instance
   of ``exe()``, it generates a new key in the given key\_path and
   encrypts the database file. This db file can henceforth only be used
   with the ``exe_secure()`` function.

Export data :
~~~~~~~~~~~~~

-  ``exportdb(export_path, sort=True)`` - Copies the entire content of
   the database file into the specified export file path using
   ``json.dump()``. To prevent sorting of Keys, use
   ``exportdb(export_path, False)``

-  ``exportmem(export_path, sort=True)`` - Copies the current database
   contents stored in-memory into the specified export file path using
   ``json.dump()``. To prevent sorting of Keys, use
   ``exportmem(export_path, False)``.

-  ``exportkeys(export_path, keys = [], sort=True)`` - Takes a list of
   keys as an argument and exports those specific keys from the
   in-memory data to the given export file path.

.. code:: python

    import elara

    db = elara.exe('new.db', False)
    db.set("one", 100)
    db.set("two", 200)
    db.commit()
    db.set("three", 300)

    db.exportdb('exportdb.txt')

    db.exportmem('exportmem.txt')
    db.exportkeys('exportkeys.txt', keys = ['one', 'three'])

    """
    # exportdb.txt
    {
        "one": 100,
        "two": 200
    }

    # exportmem.txt
    {
        "one": 100,
        "three": 300
        "two": 200
    }

    # exportkeys.txt
    {
        "one": 100,
        "three": 300
    }
    """


Tests
-----

Run this command inside the base directory to execute all tests inside
the ``test`` folder:

.. code:: sh

    $ python -m unittest -v


Dependencies
------------

-  ``cryptography``
-  ``msgpack``
-  ``safer``


Releases notes
--------------

-  Latest - ``v0.5.x``
   
   -  ``v0.5.4`` - No breaking changes 
   -  ``v0.5.3``
   -  ``v0.5.2`` 
   -  ``v0.5.1``
   -  ``v0.5.0``
  
``v0.5.x`` comes with an internal re-architecture that allows for much better caching and granular control on item expiry.
No breaking changes from ``v0.4.x``

``v0.4.x`` moves away from the json-based (``dump``, ``load``) storage approach used in earlier versions, 
instead storing it as bytes and has support for checksums and database file version flags for added security.

``v0.2.1`` and earlier used a mix of ``ascii`` and ``base64`` encoding. ``v0.3.0`` uses ``utf-8`` 
instead. 

To safeguard data, its better to export all existing data from any existing database file before upgrading Elara. 
(using ``exportdb(export_path)``)

View Elara's detailed release history
`here <https://github.com/saurabh0719/elara/releases/>`__.


Contributors 
------------

| Original author and maintainer - `Saurabh Pujari <https://github.com/saurabh0719>`__.
| Logo design - `Jonah Eapen <https://github.com/jonaheapen98>`__.

Open source contributors : 

-  `DarthUdp <https://github.com/DarthUdp>`__.
-  `AdityaKotwal100 <https://github.com/AdityaKotwal100>`__.
