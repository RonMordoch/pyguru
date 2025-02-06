import configparser
from pathlib import Path


class CredentialsFile:

    CREDENTIALS_FILEPATH = Path.home() / '.pyguru/credentials'
    DEFAULT_PROFILE_NAME = 'default'
    UNAME_KEY = 'username'
    PWD_KEY = 'password'

    @classmethod
    def load(cls, filepath: Path = None, profile_name: str = None) -> tuple[str, str]:
        filepath = filepath or cls.CREDENTIALS_FILEPATH
        profile_name = profile_name or cls.DEFAULT_PROFILE_NAME
        config = configparser.ConfigParser()
        config.read(filepath)
        return tuple(config.get(profile_name, key) for key in [cls.UNAME_KEY, cls.PWD_KEY])
