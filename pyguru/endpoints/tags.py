from pyguru.base_labguru_endpoint import BaseLabguruEndpoint


class TagsEndpoint(BaseLabguruEndpoint):

    def __init__(self, adapter) -> None:
        super().__init__(adapter, 'tags')

    def get(self):
        raise Exception('not supoorted')  # TODO

    def get_by_id(self):
        raise Exception('not supoorted')  # TODO

    # TODO this supports delete but many others dont.. maybe dont support delete by default?
