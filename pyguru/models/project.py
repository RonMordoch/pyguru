import datetime
from dataclasses import dataclass


@dataclass
class Project:
    title: str | None = None
    description: str | None = None
    start_date: datetime.date | None = None
    closed: bool | None = None
    status: str | None = None
    owner_id: int | None = None
