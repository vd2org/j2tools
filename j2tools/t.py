# Copyright (C) 2017-2019 by Vd.
# This file is part of Periodic package.
# Periodic is released under the MIT License (see LICENSE).

from jinja2 import Environment


def t_factory(env: Environment, t_variable: str = 'T', separator: str = '/'):
    def get_t(prefix: str):
        def t(template_name: str, **kwargs):
            template_name = prefix + separator + template_name
            template = env.get_template(template_name)
            if t_variable not in kwargs:
                kwargs[t_variable] = t
            return template.render(**kwargs)

        return t

    return get_t
