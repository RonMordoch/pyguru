# from pyguru.adapter import LabguruAdapter


class BaseLabguruEndpoint:

    # def __init__(self, adapter: LabguruAdapter) -> None:
    def __init__(self, adapter) -> None:
        self.adapter = adapter
