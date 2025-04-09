from http import HTTPMethod

from pyguru.credentials.credentials import Credentials
from pyguru.endpoints.sessions import SessionsEndpoint
from pyguru.request.request import Request

from .rest_adapter import RestAdapter


class LabguruAdapter(RestAdapter):

    HOST = 'my.labguru.com'
    VERSION = 'v1'

    def __init__(
        self,
        credentials: Credentials,
        host: str = HOST,
        version: str = VERSION
    ) -> None:
        # Append the /api here because its labguru specific
        super().__init__(f'{host}/api', version)
        self.credentials = credentials
        self.token = None
        self.token = self.get_token()

    def get_token(self, force: bool = False):
        if self.token and not force:
            return self.token
        return SessionsEndpoint(self).get_token(self.credentials.username, self.credentials.password)

    def pre_request_hook(self, method: HTTPMethod, request: Request):
        """
        Inject the token into the request.
        """
        if request.requires_token:
            if method == HTTPMethod.GET:  # Add token to url
                request.params = {
                    **(request.params or {}),
                    'token': self.get_token()
                }
            elif method in [HTTPMethod.POST, HTTPMethod.PUT]:  # Add token to body
                request.json = {
                    **(request.json or {}),
                    'token': self.get_token(),
                }
