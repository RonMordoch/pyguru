from dataclasses import dataclass


@dataclass
class Tag:
    tag: str | None = None
    class_name: str | None = None
    item_id: int | None = None
