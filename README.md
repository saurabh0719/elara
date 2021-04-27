<div align="center">
    <img src="elara.png" width ="75%">
    <p>ElaraDB is a Redis-inspired, easy to use key-value storage for your python projects!</p>
</div>

<hr>

```sh
$ pip install insert_here
```

## Key Features :
* Perform various operations on strings, lists and dictionaries.
* Offers two modes of execution - normal and secure - exe_secure() generates a key file and encrypts the key-value storage for additional security.
* Choose between manual commits after performing operations in-memory or automatically commit every change into the storage.
* Includes methods to export certain keys or the entire storage.
* Based on python's in-built json module for easy manipulation and access.

## Table of Contents :
* [Installation](#installation)  
* [License](#license)  
* [Usage](#usage)
    * [Basics](#basics)
    * [Strings](#strings)
    * [Lists](#lists)
    * [Dictionaries](#dict)
    * [Miscallaneous](#misc)
    * [Export](#export)
* [Tests](#tests)
* [Changelog](#change)
* [Contributing](#contr)
* [Acknowledgments](#ack)

<hr>

<span id="installation"></span>
## Installation Guide
Using pip : 
```sh
$ pip install insert_here
```
Download Source code zip *here*

<span id="license"></span>
## License 

Link to license *here*

<span id="usage"></span>
## Usage 

You can choose between normally transacting data from the file or you can transact data from an encrypted file.  

```python
>>> import elaradb as elara
# exe_secure() encrypts the db file
>>> db = elara.exe_secure("new.db", True, "newdb.key")
>>> db.set("name", "Elara")
>>> print(db.get("name"))
Elara
```

* `exe_secure(db_file_path, commit=False, key_file_path)` - Loads the contents of the encrypted database (using the key file) into the program memory or generates a new key file and/or database file if they don't exist in the given path and it encrypts/decrypts the database file. Data is encoded into a *base64* format and then encrypted using *Fernet encryption*

Using `exe_secure()` without a key file or without the correct key file corresponding to the database will result in errors. Key files and DB files can be included inside the *.gitignore* to ensure they're not pushed into an upstream repository.

* *`commit`* - this argument defaults to *`False`* ie. you will have to manually call the `commit()` method to write the in-memory changes into the database. If set to *`True`*, changes will be written into the file after every operation.

```python
>>> import elaradb as elara
>>> db = elara.exe("new.db", "newdb.key") # commit=False  
>>> db.set("num", 20)
>>> print(db.get("num"))
20
>>> db.commit() # Writes in-memory changes into the file
```

* `exe(db_file_path, commit=False)` - Loads the contents of the database into the program memory or generates a new database file if it doesn't exist in the given path. The database file is NOT encrypted and is present in a human-readable json format.

```python
>>> import elaradb as elara
>>> db = elara.exe("new.db", True)
>>> db.set("name", "Elara")
>>> print(db.get("name"))
Elara
```
<span id="basics"></span>
### Basic operations : 

All the following operations are methods that can be applied to the instance returned from `exe()` or `exe_secure()`. These operations manipulate/analyse data in-memory after the Data is loaded from the file. Set the `commit` argument to `True` else manually use the `commit()` method to sync in-memory data with the database file.

* `get(key)` - returns the corresponding value from the db or *`None`*
* `set(key, value)` - returns *`True`* or an Exception. The `key` has to be a String.
* `rem(key)` - deletes the key-value pair if it exists.
* `clear()` - clears the database data currently stored in-memory. 
* `exists(key)` - returns `True` if the key exists.
* `commit()` - write in-memory changes into the database file.
* `retkey()` - returns the Key used to encrypt/decrypt the db file, else returns *`None`* if the file is unprotected.
* `retmem()` - returns all the in-memory db contents.
* `retdb()` - returns all the db file contents. 

Note - `retmem()` and `retdb()` will return the same value if *`commit`* is set to *`True`* or if the `commit()` method is used before calling `retdb()`




