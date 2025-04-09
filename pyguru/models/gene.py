from dataclasses import dataclass


@dataclass
class Gene:
    title: str | None = None
    alternative_name: str | None = None
    expression_location: str | None = None
    pathway: str | None = None
    sequence: str | None = None
    owner_id: int | None = None
    source: str | None = None
    description: str | None = None
