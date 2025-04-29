from pyguru.base_labguru_endpoint import BaseLabguruEndpoint


class ReportsEndpoint(BaseLabguruEndpoint):

    def __init__(self, adapter) -> None:
        super().__init__(adapter, 'reports')

    def add_section(self, resource_id: int, section_id: int):
        return self.post(
            json_data={
                'resource_id': resource_id,
                'section_id': section_id
            },
            sub_route='add_section_to_report'
        )

    def add_cover(self, resource_id: int, data: str):
        return self.post(
            json_data={
                'resource_id': resource_id,
                'data': data
            },
            sub_route='add_cover_to_report'
        )
