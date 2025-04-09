from dataclasses import dataclass


@dataclass
class Visualization:
    name: str | None = None
    dataset_id: int | None = None
    attachment_id: int | None = None
