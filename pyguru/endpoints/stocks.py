from pyguru.base_labguru_endpoint import BaseLabguruEndpoint


class StocksEndpoint(BaseLabguruEndpoint):

    def __init__(self, adapter) -> None:
        super().__init__(adapter, 'stocks')

    def mark_as_consumed(self, resource_id: int):
        return self.post(sub_route=f'{resource_id}/mark_as_consumed')

    def mark_as_output(self, resource_id: int):
        return self.post(sub_route=f'{resource_id}/mark_as_output')

    def unmark_as_output(self, resource_id: int):
        return self.post(sub_route=f'{resource_id}/unmark_as_output')

    def update_stock_amount(
        self,
        resource_id: int,
        unit_type: str | None = None,  # TODO enumerate weight/volume
        element_id: int | None = None,
        amount_used: str | None = None,
        unit_type_name: str | None = None,
        subtract: str | None = None,
        sample_id: int | None = None
    ):
        return self.post(
            sub_route=f'{resource_id}/update_stock_amount',
            json_data={
                'unit_type': unit_type,
                'element_id': element_id,
                'amount_used': amount_used,
                'unit_type_name': unit_type_name,
                'subtract': subtract,
                'sample_id': sample_id
            }
        )

    def get_stocks_by_barcode(self, input: str):
        # TODO: check this works
        return self._get(sub_route='get_stocks_by_barcode', params={'input': input})
