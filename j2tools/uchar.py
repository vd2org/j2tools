# Copyright (C) 2017-2019 by Vd.
# This file is part of j2tools package.
# j2tools is released under the MIT License (see LICENSE).


import unicodedata


def uchar(*names, separator: str = '') -> str:
    """\
    Returns unicode characters by given names.
    Can be used as jinja2 filter.

    :param separator: separator for joining characters to string
    :param names: names of unicode characters
    :return: string, contains characters joined by given separator
    """
    return separator.join([unicodedata.lookup(n) for n in names])
