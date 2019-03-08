# Copyright (C) 2017-2019 by Vd.
# This file is part of j2tools package.
# j2tools is released under the MIT License (see LICENSE).


from os.path import join, dirname

import setuptools

import j2tools

setuptools.setup(
    name='j2tools',
    version=j2tools.version(),
    author='Vd',
    author_email='vd@vd2.org',
    url='https://github.com/vd2org/j2tools',
    license='MIT',
    description='Useful tools for jinja2 template processor.',
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    packages=['j2tools'],
    install_requires=open(join(dirname(__file__), 'requirements.txt')).read().split('\n'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Utilities',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Text Processing :: Markup :: HTML',
        'Topic :: Text Processing :: Markup',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Software Development :: Pre-processors',
        'Topic :: Software Development :: Localization',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
