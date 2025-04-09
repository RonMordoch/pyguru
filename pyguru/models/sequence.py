from dataclasses import dataclass

from pyguru.enums import SequenceType


@dataclass
class Sequence:
    title: str | None = None
    seq: str | None = None
    owner_id: int | None = None
    kind: SequenceType | None = None
    accsesion: str | None = None
    organism: str | None = None
    description: str | None = None
