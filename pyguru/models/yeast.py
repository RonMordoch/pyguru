from dataclasses import dataclass


@dataclass
class Yeast:
    name: str | None = None
    description: str | None = None
    reproduction: str | None = None
    genetic_background: str | None = None
    transgenic_features: str | None = None
    phenotype: str | None = None
    source: str | None = None
    owner_id: int | None = None
