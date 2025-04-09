import datetime
from dataclasses import dataclass

from pyguru.enums import StorageTypeId


@dataclass
class Stock:
    name: str | None = None
    storage_id: StorageTypeId | None = None
    # TODO enum storage class name - [Box - System::Storage::Box] [all other storages type - System::Storage::Storage]
    storage_type: str | None = None
    stockable_type: str | None = None
    stockable_id: int | None = None
    location_in_box: int | None = None
    owner_id: int | None = None
    expiration_date: datetime.date | None = None
    lot: str | None = None
    description: str | None = None
    barcode: str | None = None
    stored_by: int | None = None
    concentration: str | None = None
    concentration_prefix: str | None = None
    concentration_unit_id: int | None = None
    concentration_exponent: int | None = None
    concentration_remarks: str | None = None
    volume: str | None = None
    volume_prefix: str | None = None
    volume_unit_id: int | None = None
    volume_exponent: int | None = None
    volume_remarks: str | None = None
    weight: str | None = None
    weight_prefix: str | None = None
    weight_unit_id: int | None = None
    weight_exponent: int | None = None
    weight_remarks: str | None = None
