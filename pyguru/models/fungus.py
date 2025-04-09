from dataclasses import dataclass


@dataclass
class Fungus:
    name: str | None = None
    species: str | None = None
    phenotype: str | None = None
    genotype: str | None = None
    host: str | None = None
    virulent: str | None = None
    sporulate: str | None = None
    mycelia: str | None = None
    fruiting_bodies: str | None = None
    owner_id: int | None = None
    source: str | None = None
    description: str | None = None
