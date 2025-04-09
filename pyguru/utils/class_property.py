class classproperty(object):
    """
    A decorator for class property, supporting only getter.
    """

    def __init__(self, f):
        self.get_func = f

    def __get__(self, obj, owner):
        return self.get_func(owner)
