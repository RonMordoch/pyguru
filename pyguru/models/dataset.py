from dataclasses import dataclass


@dataclass
class Dataset:
    name: str | None = None
    data_attachment_id: int
    sdf_attachment_id: int | None = None
    description: str | None = None
