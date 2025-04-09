import datetime
from dataclasses import dataclass


@dataclass
class Plant:
    name: str | None = None
    owner_id: int | None = None
    phenotype: str | None = None
    genotype: str | None = None
    generation: str | None = None
    harvest_date: datetime.date | None = None
    source: str | None = None
    description: str | None = None
