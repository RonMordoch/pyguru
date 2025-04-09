from pyguru.base_labguru_endpoint import BaseLabguruEndpoint


class BiocollectionsEndpoint(BaseLabguruEndpoint):
    """
    Appears as "Submodules" in the API specification:
    https://my.labguru.com/api-docs/index.html#/Submodules
    """

    def __init__(self, adapter, biocollection: str) -> None:
        super().__init__(adapter, f'biocollections/{biocollection}')

    def get_derived_collections(self):
        return self._get(sub_route='get_derived_collections')

    def get_derived_items(
        self,
        item_id: int,
        derived_collection_name: str,
        derived_collection_id: int | None = None
    ):
        params = {
            'derived_collection_name': derived_collection_name,
        }
        if derived_collection_id is not None:
            params['derived_collection_id'] = derived_collection_id
        return self._get(sub_route=f'{item_id}/get_derived_items', params=params)
