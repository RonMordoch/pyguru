from dataclasses import dataclass

from pyguru.enums import Currency


@dataclass
class StandardShoppingList:
    collection_type: str | None = None
    item_id: int | None = None
    quantity: int | None = None
    price: float | None = None
    currency: Currency | None = None
    remarks: str | None = None


@dataclass
class CustomShoppingList(StandardShoppingList):
    collection_id: int | None = None
