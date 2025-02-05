from pyguru.credentials.credentials import Credentials
from pyguru.endpoints.auth import AuthEndpoint

from .rest_adapter import RestAdapter


class LabguruAdapter(RestAdapter):

    HOST = 'my.labguru.com/api'
    VERSION = 'v1'

    def __init__(self, credentials: Credentials) -> None:
        super().__init__(self.HOST, self.VERSION)
        self.credentials = credentials
        self.token = None
        self.token = self.get_token(force=True)  # TODO this aint pretty!

    def get_token(self, force: bool = False):
        if self.token and not force:
            return self.token
        return AuthEndpoint(self).get_token(self.credentials.username, self.credentials.password)
