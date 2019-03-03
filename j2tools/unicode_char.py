# Copyright (C) 2017-2019 by Vd.
# This file is part of j2tools package.
# Periodic is released under the MIT License (see LICENSE).


import unicodedata


def unicode_char(*names):
    return ''.join([unicodedata.lookup(n) for n in names])
