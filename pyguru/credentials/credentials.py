from pyguru.utils.env import Env

from .credentials_data import CredentialsData
from .credentials_file import CredentialsFile


class MissingCredentials(Exception):
    pass


class Credentials:

    def __init__(
        self,
        username: str | None = None,
        password: str | None = None,
        host: str | None = None,
        profile_name: str | None = None
    ) -> None:
        self.data: CredentialsData = self.load_credentials(username, password, host, profile_name)
        # self.username, self.password = self.load_credentials(username, password, profile_name)
        # self.profile_name = profile_name

    @property
    def token(self):
        """
        Small wrapper over the token environment variable to consolidate all credentials-related access to this class.
        """
        return Env.PYGURU_TOKEN

    def load_env_credentials(self) -> CredentialsData:
        return CredentialsData(
            username=Env.PYGURU_USERNAME,
            password=Env.PYGURU_PASSWORD,
            host=Env.PYGURU_HOST,
            profile_name=Env.PYGURU_PROFILE
        )

    def load_credentials(
        self,
        username: str | None = None,
        password: str | None = None,
        host: str | None = None,
        profile_name: str | None = None
    ) -> tuple[str, str]:
        """
        PyGuru will search for credentials in the following order:
        1. Constructor parameters
        2. Environment variables.
        3. A credentials file as defined in `CredentialsFile` using profile name.
            ```
        """
        if username and password:
            return CredentialsData(
                username=username,
                password=password,
                host=host,
                profile_name=profile_name
            )
        elif Env.PYGURU_USERNAME:
            return self.load_env_credentials()
        elif CredentialsFile.CREDENTIALS_FILEPATH.exists():
            return CredentialsFile.load(profile_name=profile_name)
        else:
            raise MissingCredentials('Credentials not found!')
