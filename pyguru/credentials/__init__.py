from pyguru.utils.env import Env

from .credentials import Credentials, MissingCredentials
from .credentials_file import CredentialsFile


def load_env_credentials() -> Credentials:
    return Credentials(
        username=Env.PYGURU_USERNAME,
        password=Env.PYGURU_PASSWORD,
        host=Env.PYGURU_HOST,
        profile=Env.PYGURU_PROFILE,
        account_id=Env.PYGURU_ACCOUNT
    )


def load_credentials(
    username: str | None = None,
    password: str | None = None,
    host: str | None = None,
    profile: str | None = None,
    account_id: int | None = None
) -> tuple[str, str]:
    """
    PyGuru will search for credentials in the following order:
    1. Constructor parameters
    2. Environment variables.
    3. A credentials file as defined in `CredentialsFile` using profile name.
        ```
    """
    if username and password:
        return Credentials(
            username=username,
            password=password,
            host=host,
            profile=profile,
            account_id=account_id
        )
    elif Env.PYGURU_USERNAME:
        return load_env_credentials()
    elif CredentialsFile.CREDENTIALS_FILEPATH.exists():
        return CredentialsFile.load(profile=profile)
    else:
        raise MissingCredentials('Credentials not found!')
