import os

from pyguru.utils.class_property import classproperty


class Env:

    @classproperty
    def PYGURU_USERNAME(self):
        return os.environ.get('PYGURU_USERNAME')

    @classproperty
    def PYGURU_PASSWORD(self):
        return os.environ.get('PYGURU_PASSWORD')

    @classproperty
    def PYGURU_TOKEN(self):
        return os.environ.get('PYGURU_PASSWORD')
