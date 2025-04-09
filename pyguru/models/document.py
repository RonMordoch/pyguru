from dataclasses import dataclass


@dataclass
class Document:
    title: str | None = None
    description: str | None = None
