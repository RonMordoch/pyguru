import os

from pyguru.utils.class_property import classproperty


class Env:

    @classproperty
    def PYGURU_PROFILE(self):
        return os.environ.get('PYGURU_PROFILE')

    @classproperty
    def PYGURU_HOST(self):
        return os.environ.get('PYGURU_HOST')

    @classproperty
    def PYGURU_ACCOUNT(self):
        return os.environ.get('PYGURU_ACCOUNT')

    @classproperty
    def PYGURU_USERNAME(self):
        return os.environ.get('PYGURU_USERNAME')

    @classproperty
    def PYGURU_PASSWORD(self):
        return os.environ.get('PYGURU_PASSWORD')

    @classproperty
    def PYGURU_TOKEN(self):
        return os.environ.get('PYGURU_TOKEN')
