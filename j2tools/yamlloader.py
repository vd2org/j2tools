import logging
from os.path import exists, getmtime

from jinja2 import BaseLoader, TemplateNotFound
from ruamel.yaml import load, BaseLoader as Loader

# from yaml import load
# try:
#     from yaml import CLoader as Loader
# except ImportError:
#     from yaml import Loader

logger = logging.getLogger('j2tools.yamlloader')


class YamlLoader(BaseLoader):
    def __init__(self, path, separator='/'):
        self.path = path
        self.separator = separator
        self.__data = dict()
        self.__mtime = None

    def get_source(self, environment, template):
        mtime = getmtime(self.path)
        if self.__mtime != mtime:
            self.__mtime = mtime
            if not exists(self.path):
                raise TemplateNotFound(template)
            with open(self.path, 'r') as f:
                self.__data = load(f, Loader=Loader)

        source = self.__data
        for i in template.split(self.separator):
            if type(source) is not dict:
                raise TemplateNotFound(template)
            source = source.get(i)

        if type(source) is not str:
            raise TemplateNotFound(template)

        p = "{}:{}".format(self.path, template)
        return source, p, lambda: mtime == getmtime(self.path)
