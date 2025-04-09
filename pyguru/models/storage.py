from dataclasses import dataclass

from pyguru.enums import StorageTypeId


@dataclass
class Storage:
    name: str | None = None
    storage_type_id: StorageTypeId | None = None
    description: str | None = None
    temperature: int | None = None
