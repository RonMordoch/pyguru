from pyguru.base_labguru_endpoint import BaseLabguruEndpoint


class LipidsEndpoint(BaseLabguruEndpoint):

    def __init__(self, adapter) -> None:
        super().__init__(adapter, 'lipids')
