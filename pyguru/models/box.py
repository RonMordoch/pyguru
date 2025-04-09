from dataclasses import dataclass

from pyguru.enums import BoxType, Color


@dataclass
class Box:
    box_id: int
    name: str | None = None
    rows: int | None = None
    cols: int | None = None
    box_type: BoxType | None = None
    color: Color | None = None
    shared: bool | None = None
    barcode: str | None = None
