from dataclasses import dataclass

from pyguru.utils.env import Env


class MissingCredentials(Exception):
    pass


@dataclass
class Credentials:

    username: str
    password: str
    host: str | None = None
    profile_name: str | None = None
    account_id: int | None = None

    def __post_init__(self):
        if self.account_id is not None:
            self.account_id = int(self.account_id)

    @property
    def token(self):
        """
        Small wrapper over the token environment variable to consolidate all credentials-related access to this class.
        """
        return Env.PYGURU_TOKEN
