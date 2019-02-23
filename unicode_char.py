import unicodedata


def unicode_char(*names):
    return ''.join([unicodedata.lookup(n) for n in names])
