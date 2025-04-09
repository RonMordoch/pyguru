import datetime
from dataclasses import dataclass

from pyguru.enums import Clonality


@dataclass
class Antibody:
    title: str | None = None
    owner_id: int | None = None
    alternative_name: str | None = None
    antigene: str | None = None
    tags_fluorophores: str | None = None
    clone_field: str | None = None
    isotype: str | None = None
    preparation_date: datetime.datetime | None = None
    source: str | None = None
    immune: Clonality | None = None
    organism_id: int | None = None
    reacts_with: str | None = None
    description: str | None = None
