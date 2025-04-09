from dataclasses import dataclass


@dataclass
class Webhook:
    trigger_key: str | None = None
    active: bool | None = None
    url: str | None = None
