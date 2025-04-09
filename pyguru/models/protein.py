from dataclasses import dataclass


@dataclass
class Protein:
    name: str | None = None
    owner_id: int | None = None
    alternative_name: str | None = None
    gene: str | None = None
    species: str | None = None
    lg_mutations: str | None = None
    chemical_modifications: str | None = None
    tag: str | None = None
    purification_method: str | None = None
    mw: str | None = None
    extinction_coefficient_280nm: str | None = None
    storage_buffer: str | None = None
    storage_temperature: str | None = None
    source: str | None = None
    sequence: str | None = None
    description: str | None = None
