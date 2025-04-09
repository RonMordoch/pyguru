import datetime
from dataclasses import dataclass


@dataclass
class Tissue:
    name: str | None = None
    alternative_name: str | None = None
    species: str | None = None
    genotype_phenotype: str | None = None
    animal_details: str | None = None
    tissue_type: str | None = None
    harvest_date: datetime.date | None = None
    fixation_embedding_procedure: str | None = None
    applications: str | None = None
    storage_conditions: str | None = None
    owner_id: int | None = None
    source: str | None = None
    description: str | None = None
