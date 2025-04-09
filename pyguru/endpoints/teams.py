from pyguru.base_labguru_endpoint import BaseLabguruEndpoint


class TeamsEndpoint(BaseLabguruEndpoint):

    def __init__(self, adapter) -> None:
        super().__init__(adapter, 'teams')
    # TODO model class
