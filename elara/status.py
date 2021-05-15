"""
Copyright (c) 2021, Saurabh Pujari
All rights reserved.

This source code is licensed under the BSD-style license found in the LICENSE file in the root directory of this source tree.
"""

from enum import Enum


class Status(Enum):
    EXPIRED = -1
    FULL = -2
    NOTFOUND = -3


# class cache_obj:
#     def __init__(self, key, max_age):
#         self.key = key
#         self.max_age = max_age

# obj1 = cache_obj("one", 1)
# obj2 = cache_obj("two", 2)

# new_list = []

# new_list.append(obj1)
# new_list.append(obj2)

# if obj1.key in new_list:
#     print("Its there lol")

# cache_param = {
#     "max_age" : 3600,
#     "max_size" : 1000
# }

# print(cache_param["max_age"])

# if "max_age" in cache_param:
#     print(cache_param["max_size"])
