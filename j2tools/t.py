# Copyright (C) 2017-2019 by Vd.
# This file is part of j2tools package.
# j2tools is released under the MIT License (see LICENSE).


import typing
from jinja2 import Environment


def t_factory(env: Environment, t_variable: str = 'T', separator: str = '/') -> typing.Callable:
    """\
    Factory function that returns helper
    that helps loading multipath templates.
    Useful in case when you using separate template
    files for each language. Very useful with YamlLoader.

    Example usage:

        #setup jinja2
        jinja = jinja2.Environment(...)
        get_t = t_factory(jinja)
        ...

        #get t-functions
        templates_en = get_t('en')
        templates_jp = get_t('jp')
        ...

        #get template and render it
        rendered = templates_en('some/template/path', username=username)

    :param env: jinja2 environment
    :param t_variable: T-variable name to set as template parameter
    :param separator: template path separator
    :return:
    """

    def get_t(prefix: str) -> typing.Callable:
        def t(template_name: str, **kwargs):
            template_name = prefix + separator + template_name
            template = env.get_template(template_name)
            if t_variable not in kwargs:
                kwargs[t_variable] = t
            return template.render(**kwargs)

        return t

    return get_t
