# Copyright (C) 2017-2019 by Vd.
# This file is part of j2tools package.
# j2tools is released under the MIT License (see LICENSE).


from .plural import plural, languages
from .t import t_factory
from .uchar import uchar
from .elapsed import elapsed, remaining
from .yamlloader import YamlLoader


def version():
    return "2019.03"
