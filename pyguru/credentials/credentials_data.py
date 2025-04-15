from dataclasses import dataclass


@dataclass
class CredentialsData:
    username: str
    password: str
    host: str | None = None
    profile_name: str | None = None
