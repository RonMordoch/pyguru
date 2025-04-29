from pyguru.base_labguru_endpoint import BaseLabguruEndpoint
from pyguru.enums.element_type import ElementType


class ExperimentsEndpoint(BaseLabguruEndpoint):

    def __init__(self, adapter) -> None:
        super().__init__(adapter, 'experiments')

    def get(self):
        raise Exception('not supported')  # TODO custom exception

    def get_experiment_elements(
        self,
        experiment_id: int,
        element_type: ElementType | None = None,
        name: str | None = None,
    ):
        return self.get(
            sub_route=f'{experiment_id}/elements',
            params={
                'name': name,
                'element_type': element_type
            }
        )

    def add_flag(
        self,
        experiment_id: int,
        flag_id: int
    ):
        return self.post(
            json_data={
                'flag_id': flag_id
            },
            sub_route=f'{experiment_id}/set_flag_as'
        )
