import os

from .credentials_file import CredentialsFile


class MissingCredentials(Exception):
    pass


class Credentials:

    ENV_VAR_UNAME = 'PYGURU_USERNAME'
    ENV_VAR_PWD = 'PYGURU_PASSWORD'

    def __init__(self, username: str = None, password: str = None, profile_name: str = CredentialsFile.DEFAULT_PROFILE_NAME) -> None:
        self.username, self.password = self.load_credentials(username, password, profile_name)
        self.profile_name = profile_name

    def load_credentials(self, username: str = None, password: str = None, profile_name: str = None) -> tuple[str, str]:
        """
        PyGuru will search for credentials in the following order:
        1. Username and password as constructor parameters
        2. Username and password in the environment variables PYGURU_USERNAME and PYGURU_PASSWORD, respectively.
        3. A credentials file located in `~/.pyguru/credentials` in the format of:
            ```
            [DEFAULT] <-- Or any other profile
            username=<username>
            password=<password>
            ```
        """
        if username and password:
            return username, password
        if (
            (env_username := os.environ.get(self.ENV_VAR_UNAME))
            and
            (env_password := os.environ.get(self.ENV_VAR_PWD))
        ):
            return env_username, env_password
        elif CredentialsFile.CREDENTIALS_FILEPATH.exists():
            return CredentialsFile.load(profile_name=profile_name)
        else:
            raise MissingCredentials('Credentials not found!')
