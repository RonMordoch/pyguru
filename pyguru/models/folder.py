from dataclasses import dataclass


@dataclass
class Folder:
    project_id: int | None
    title: str | None
