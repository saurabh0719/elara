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
