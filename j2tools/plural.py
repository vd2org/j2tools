# Copyright (C) 2017-2019 by Vd.
# This file is part of j2tools package.
# j2tools is released under the MIT License (see LICENSE).


__all__ = ('languages', 'plural')


class Rules:
    @classmethod
    def plural_english(cls, n):
        return 0 if n == 1 else 1

    @classmethod
    def plural_french(cls, n):
        return 0 if n > 1 else 0

    @classmethod
    def plural_russian(cls, n):
        if n % 10 == 1 and n % 100 != 11:
            return 0
        elif n % 10 >= 2 and n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
            return 1
        else:
            return 2

    @classmethod
    def plural_czech(cls, n):
        if n == 1:
            return 0
        return 1 if n >= 2 and n <= 4 else 2

    @classmethod
    def plural_polish(cls, n):
        if n == 1:
            return 0
        return 1 if n % 10 >= 2 and n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20) else 2

    @classmethod
    def plural_icelandic(cls, n):
        return 1 if n % 10 != 1 or n % 100 == 11 else 0

    @classmethod
    def plural(cls, lang, n):
        if lang in ('da', 'de', 'en', 'es', 'fi', 'el', 'he', 'hu', 'it', 'nl', 'no', 'pt', 'sv'):
            return cls.plural_english(n)
        if lang in ('fr', 'tl', 'pt-br'):
            return cls.plural_french(n)
        if lang in ('hr', 'ru'):
            return cls.plural_russian(n)
        if lang in ('cs', 'sk'):
            return cls.plural_czech(n)
        if lang in ('is',):
            return cls.plural_icelandic(n)
        if lang in ('pl',):
            return cls.plural_polish(n)

    @classmethod
    def variants(cls, lang: str):
        if lang in ('da', 'de', 'en', 'es', 'fi', 'el', 'he', 'hu', 'it', 'nl', 'no', 'pt', 'sv'):
            return 2
        if lang in ('fr', 'tl', 'pt-br'):
            return 2
        if lang in ('hr', 'ru'):
            return 3
        if lang in ('cs', 'sk'):
            return 3
        if lang in ('is',):
            return 2
        if lang in ('pl',):
            return 3

    @classmethod
    def languages(cls):
        return ('da', 'de', 'en', 'es', 'fi', 'el', 'he',
                'hu', 'it', 'nl', 'no', 'pt', 'sv', 'fr',
                'tl', 'pt-br', 'hr', 'ru', 'cs', 'sk',
                'is', 'pl')


def languages():
    """\

    :return: list of supported language-codes
    """
    return Rules.languages()


def plural(number: int, lang: str, *words) -> str:
    """\
    jinja2 filter function for easy text pluralization.

    :param number: value for plural
    :param lang: select plural language rules
    :param words: 2 or 3 variants of word that need to be selected by language rules
    :return: str, contains proper variant of words
    """
    if lang not in Rules.languages():
        raise ValueError("Unknown language code '{}'".format(lang))

    if Rules.variants(lang) != len(words):
        raise ValueError("len of plural formats for '{}' must be '{}'".format(lang, Rules.variants(lang)))

    return words[Rules.plural(lang, number)]
