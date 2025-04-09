from dataclasses import dataclass


@dataclass
class Experiment:
    title: str | None = None
    project_id: int | None = None
    milestone_id: int | None = None
    protocol_id: int | None = None
