from dataclasses import dataclass


@dataclass
class Compound:
    name: str | None = None
    description: str | None = None
    structure: str | None = None
    cas: str | None = None
    formula: str | None = None
    molar_mass: str | None = None
    density: str | None = None
    melting_point: str | None = None
    hazards: str | None = None
