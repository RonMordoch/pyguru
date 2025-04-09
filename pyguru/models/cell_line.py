from dataclasses import dataclass


@dataclass
class CellLine:
    name: str | None = None
    owner_id: int | None = None
    organism: str | None = None
    tissue: str | None = None
    medium_and_serum: str | None = None
    source: str | None = None
    description: str | None = None
