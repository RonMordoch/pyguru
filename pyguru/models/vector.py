from dataclasses import dataclass


@dataclass
class Vector:
    dataset_id: int | None = None
    vector_data: dict[str, str] | None = None
