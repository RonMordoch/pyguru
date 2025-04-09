from dataclasses import dataclass


@dataclass
class Unit:
    name: str | None = None
    type_for: str | None = None
