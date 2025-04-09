from dataclasses import dataclass


@dataclass
class Virus:
    name: str | None = None
    alternative_name: str | None = None
    gene_insert: str | None = None
    virus_type: str | None = None
    plasmid: str | None = None
    serotype_strain: str | None = None
    mutations_deletions: str | None = None
    tag: str | None = None
    selectable_marker: str | None = None
    producer_cell_type: str | None = None
    viral_coat: str | None = None
    tropism: str | None = None
    species: str | None = None
    safety_information: str | None = None
    storage_conditions: str | None = None
    owner_id: int | None = None
    source: str | None = None
    description: str | None = None
