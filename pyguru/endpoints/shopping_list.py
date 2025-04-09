from pyguru.base_labguru_endpoint import BaseLabguruEndpoint
from pyguru.enums import Currency


class ShoppingListEndpoint(BaseLabguruEndpoint):

    def __init__(self, adapter) -> None:
        super().__init__(adapter, 'shopping_list')

    # TODO update model class, its missing "budget", "order_number", "description"
    # def update(
    #     self,
    #     shopping_list_id: int,
    #     budget: str | None = None,
    #     price: float | None = None,
    #     currency: Currency | None = None,
    #     quantity: int | None = None,
    #     order_number: int | None = None,
    #     description: str | None = None
    # ):

    def approve(self, shopping_list_id: int):
        return self.put(resource_id=shopping_list_id, sub_route='approve')

    def cancel(self, shopping_list_id: int):
        return self.put(resource_id=shopping_list_id, sub_route='cancel')

    def submit(self, shopping_list_id: int):
        return self.put(resource_id=shopping_list_id, sub_route='submit')
