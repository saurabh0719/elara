Elara :
-------

- Elara DB is an easy to use, key-value database written for python that can also be used as a fast in-memory cache. Includes various methods to manipulate data structures in-memory, secure database files and export data.

.. code:: sh

    $ pip install elara


Key Features :
--------------

-  Offers two modes of execution - normal and secure - exe\_secure()
   generates a key file and encrypts the key-value storage for
   additional security.
-  Manipulate data structures in-memory.
-  Can be used as a fast in-memory cache.
-  Choose between manual commits after performing operations in-memory
   or automatically commit every change into the storage.
-  Includes methods to export certain keys from the database or the
   entire storage.
-  Based on python's in-built json module for easy manipulation and
   access.


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

Usage
-----

Basic usage :
~~~~~~~~~~~~~

You can choose between normally transacting data from the file or you
can transact data from an encrypted file.

.. code:: python

    import elara

    # exe_secure() encrypts the db file
    db = elara.exe_secure("new.db", True, "newdb.key")

    db.set("name", "Elara")

    print(db.get("name"))
    # Elara

-  ``exe_secure(db_file_path, commit=False, key_file_path)`` - Loads the
   contents of the encrypted database (using the key file) into the
   program memory or generates a new key file and/or database file if
   they don't exist in the given path and it encrypts/decrypts the
   database file. Data is encoded into a *base64* format and then
   encrypted using *Fernet encryption*

Using ``exe_secure()`` without a key file or without the correct key
file corresponding to the database will result in errors. Key files and
DB files can be included inside the *.gitignore* to ensure they're not
pushed into an upstream repository.

-  *``commit``* - this argument defaults to *``False``* ie. you will
   have to manually call the ``commit()`` method to write the in-memory
   changes into the database. If set to *``True``*, changes will be
   written into the file after every operation.

.. code:: python

    import elara

    db = elara.exe("new.db", "newdb.key") # commit=False  

    db.set("num", 20)

    print(db.get("num"))
    # 20

    db.commit() # Writes in-memory changes into the file

-  ``exe(db_file_path, commit=False)`` - Loads the contents of the
   database into the program memory or generates a new database file if
   it doesn't exist in the given path. The database file is NOT
   encrypted and is present in a human-readable json format.

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
   *``None``*
-  ``set(key, value)`` - returns *``True``* or an Exception. The ``key``
   has to be a String.
-  ``rem(key)`` - deletes the key-value pair if it exists.
-  ``clear()`` - clears the database data currently stored in-memory.
-  ``exists(key)`` - returns *``True``* if the key exists.
-  ``commit()`` - write in-memory changes into the database file.
-  ``getset(key, value)`` - Sets the new value and returns the old value
   for that key or returns *``False``*.
-  ``getkeys()`` - returns the list of keys in the database with. The
   list is ordered with the *``least recently accessed``* keys starting
   from index 0.
-  ``numkeys()`` - returns the number of keys in the database.
-  ``retkey()`` - returns the Key used to encrypt/decrypt the db file;
   returns *``None``* if the file is unprotected.
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
*``commit``* is set to *``True``* or if the ``commit()`` method is used
before calling ``retdb()``

Cache:
~~~~~~

Elara can also be used as a fast in-memory cache. Start/open a new
instance and ensure the ``commit`` argument is *``False``* or left empty
(``commit`` defaults to ``False``), to prevent writes into the database
file.

-  ``cull(percentage)`` - ``percentage`` (0 <= percentage <= 100)
   defines the percentage of Key-Value pairs to be deleted, with the
   *Least recently accessed* keys being deleted first. Elara maintains a
   simple LRU list to track key access.

.. code:: python

    import elara

    cache = elara.exe("new.db")

    cache.set("num1", 10)
    cache.set("num2", 20)
    cache.set("num3", 30)
    cache.set("num4", 40)

    if cache.exists("num1"):
        print(cache.get("num1"))
        # 10 
        
    print(cache.retmem())
    # {'num1': 10, 'num2': 20, 'num3': 30, 'num4': 40}

    # least recently accessed keys come first
    print(cache.getkeys())
    # ['num1', 'num4', 'num3', 'num2']

    # delete 25% of the stale keys (follows LRU)
    cache.cull(25) 

    # least recently accessed keys come first
    print(cache.getkeys())
    # ['num1', 'num4', 'num3']

API
---

Strings :
~~~~~~~~~

-  ``mget(keys)`` - takes a list of keys as an argument and returns a
   list with all the corresponding values IF they exist; returns an
   empty list otherwise.
-  ``mset(dict)`` - takes a dictionary of key-value pairs as an argument
   and calls the ``set(key, value)`` method for each pair. Keys have to
   be a String.
-  ``setnx(key, value)`` - Sets the key-value if the key does not exist
   and returns *``True``*; returns *``False``* otherwise.
-  ``msetnx(dict)`` - takes a dictionary of key-value pairs as an
   argument and calls the ``setnx(key, value)`` method for each pair.
   Keys have to be a string.
-  ``slen(key)`` - returns the length of the string value if the key
   exists; returns ``-1`` otherwise.
-  ``append(key, data)`` - Append the data (String) to an existing
   string value; returns *``False``* if it fails.

Lists :
~~~~~~~

-  ``lnew(key)`` - Initialises an empty list for the given key and
   returns ``True`` or an Exception; key has to be a string.
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

    db = elara.exe('new.db', True)

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

| => The following methods do not have complete test coverage yet :
| 

Hashtable/Dictionary :
~~~~~~~~~~~~~~~~~~~~~~

-  ``hnew(key)`` - Initialises an empty dictionary for the given key and
   returns ``True`` or an Exception; key has to be a string.
-  ``hadd(key, dict_key, value)`` - Assigns a value to a dictionary key
   and returns *``True``*; returns *``False``* if the dictionary doesn't
   exist.
-  ``haddt(key, tuple)`` - Add a new key-value tuple into the
   dictionary. Returns *``True``* if the dictionary exists; returns
   *``False``* otherwise.
-  ``hget(key, dict_key)`` - Returns the value from the dictionary;
   returns *``False``* if the dictionary doesn't exist.
-  ``hpop(key, dict_key)`` - Deletes the given key-value pair from the
   dictionary and returns the deleted value; returns *``False``* if the
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

    '''
    # exportdb.txt
    {
        "one": 100,
        "two": 200
    }

    # exportmem.txt
    {
        "one": 100,
        "two": 200,
        "three": 300
    }

    # exportkeys.txt
    {
        "one": 100,
        "three": 300
    }
    '''


Tests :
~~~~~~~

Run this command inside the base directory to execute all tests inside
the ``test`` folder:

.. code:: sh

    $ python -m unittest -v


Releases :
~~~~~~~~~~

-  Latest - ``v0.2.0``
-  Previous - ``v0.1.3``

Donwload the latest release from
`here <https://github.com/saurabh0719/elara/releases/>`__.


Contributors :
~~~~~~~~~~~~~~

| Author - Saurabh Pujari
| 
| Logo design - Jonah Eapen
