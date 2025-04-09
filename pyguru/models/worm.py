from dataclasses import dataclass


@dataclass
class Worm:
    name: str | None = None
    alternative_name: str | None = None
    gene_id: int | None = None
    source: str | None = None
    genotype: str | None = None
    phenotype: str | None = None
    mutagen: str | None = None
    growth_conditions: str | None = None
    outcrossed: int | None = None
    made_by: str | None = None
    dauer_defective: int | None = None
    description: str | None = None