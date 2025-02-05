import configparser
from pathlib import Path


class CredentialsFileParser:

    CREDENTIALS_FILEPATH = Path.home() / '.pyguru/credentials'
    DEFAULT_PROFILE_NAME = 'default'
    UNAME_KEY = 'username'
    PWD_KEY = 'password'

    @classmethod
    def parse(cls, filepath: Path = CREDENTIALS_FILEPATH, profile_name=DEFAULT_PROFILE_NAME) -> tuple[str, str]:
        config = configparser.ConfigParser()
        config.read(filepath)
        return tuple(config.get(profile_name, key) for key in [cls.UNAME_KEY, cls.PWD_KEY])
