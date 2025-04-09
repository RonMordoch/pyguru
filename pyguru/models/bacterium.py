from dataclasses import dataclass


@dataclass
class Bacterium:
    name: str | None = None
    sensitivity: str | None = None
    strain: str | None = None
    source: str | None = None
    owner_id: int | None = None
    description: str | None = None
