import configparser
from pathlib import Path

from .credentials import Credentials


class CredentialsFile:
    """
    File format should be:
    ```
    [default] <-- Or any other profile name
    username=<username>
    password=<password>
    host=<host>
    ```
    `host` key is optional.
    """

    CREDENTIALS_FILEPATH = Path.home() / '.pyguru/credentials'
    DEFAULT_PROFILE_NAME = 'default'
    UNAME_KEY = 'username'
    PWD_KEY = 'password'
    HOST_KEY = 'host'
    ACCOUNT_KEY = 'account'

    @classmethod
    def load(cls, filepath: Path = None, profile_name: str = None) -> Credentials:
        filepath = filepath or cls.CREDENTIALS_FILEPATH
        profile_name = profile_name or cls.DEFAULT_PROFILE_NAME
        config = configparser.ConfigParser()
        config.read(filepath)
        return Credentials(
            username=config.get(profile_name, cls.UNAME_KEY),
            password=config.get(profile_name, cls.PWD_KEY),
            host=config.get(profile_name, cls.HOST_KEY, fallback=None),
            account_id=config.get(profile_name, cls.ACCOUNT_KEY, fallback=None),
            profile_name=profile_name
        )

    @classmethod
    def write(
        cls,
        username: str,
        password: str,
        host: str | None = None,
        profile_name: str | None = None,
        account_id: int | None = None,
        filepath: Path = None
    ):
        """
        Writes the given credentials into the specified file path, appending the data if file exists.
        If profile name exists, it will overwrite the existing credentials with the given ones.
        """
        filepath = filepath or cls.CREDENTIALS_FILEPATH
        profile_name = profile_name or cls.DEFAULT_PROFILE_NAME
        config = configparser.ConfigParser()
        if filepath.exists():
            # Reading the config beforehand makes sure we will don't remove data from non-conflicting profiles
            config.read(filepath)
        profile_config = {
            cls.UNAME_KEY: username,
            cls.PWD_KEY: password,
            cls.HOST_KEY: host,
            cls.ACCOUNT_KEY: account_id
        }
        profile_config = {k: v for k, v in profile_config.items() if v is not None}
        config[profile_name] = profile_config
        with filepath.open('w') as f:
            config.write(f)
