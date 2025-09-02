from pyguru.base_labguru_endpoint import BaseLabguruEndpoint


class SectionsEndpoint(BaseLabguruEndpoint):

    def __init__(self, adapter) -> None:
        super().__init__(adapter, 'sections')

    def sort(self, container_id: int, container_type: str, ids: list):
        return self.post(
            json_data={
                'container_id': container_id,
                'container_type': container_type,
                'list': ids
            },
            sub_route='sort'
        )
