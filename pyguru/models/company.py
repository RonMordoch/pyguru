from dataclasses import dataclass


@dataclass
class Company:
    name: str | None = None
    address: str | None = None
    web: str | None = None
    contact: str | None = None
    email: str | None = None
    fax: str | None = None
    description: str | None = None
