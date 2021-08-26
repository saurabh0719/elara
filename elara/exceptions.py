"""
Copyright (c) 2021, Saurabh Pujari
All rights reserved.

This source code is licensed under the BSD-style license found in the LICENSE file in the root directory of this source tree.
"""


# Add all custom exception classes here


class FileAccessError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"Error -> {self.message}"


class FileKeyError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"Error -> {self.message}"


class InvalidCacheParams(Exception):
    def __init__(self, message):
        self.message = "Invalid Cache parameters provided - " + message

    def __str__(self):
        return f"Error -> {self.message}"


class LoadChecksumError(Exception):
    pass


class LoadIncompatibleDB(Exception):
    pass


class InvalidKeyError(Exception):
    pass