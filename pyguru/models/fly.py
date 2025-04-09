from dataclasses import dataclass


@dataclass
class Fly:
    name: str | None = None
    owner_id: int | None = None
    source: str | None = None
    genotype: str | None = None
    phenotype: str | None = None
    breakpoints_insertions: str | None = None
    ch_number: str | None = None
    ch_te: str | None = None
    description: str | None = None
