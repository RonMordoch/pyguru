import json
from http import HTTPMethod

from pyguru.credentials.credentials import Credentials
from pyguru.endpoints.sessions import SessionsEndpoint
from pyguru.request.request import Request

from .rest_adapter import RestAdapter


class LabguruAdapter(RestAdapter):

    def __init__(
        self,
        credentials: Credentials,
        host: str,
        version: str
    ) -> None:
        # Append the /api here because its labguru specific
        super().__init__(f'{host}/api', version)
        self.credentials = credentials
        self.token = None

    def get_token(self, force: bool = False):
        """
        Returns an API token by the following order:
        1. Existing, previously-defined token in the class.
        2. Token defined in an environment variable.
        3. Newly fetched token from the API endpoint.
        """
        if self.credentials.token:  # Note: this will use the environment variable if existing, before all other methods
            return self.credentials.token
        elif self.token and not force:
            return self.token
        return SessionsEndpoint(self).get_token(self.credentials.username, self.credentials.password, self.credentials.account_id)

    def pre_request_hook(self, method: HTTPMethod, request: Request):
        """
        Inject the token into the request and format params if needed for GET requests.
        """
        # LabGuru API expects nested dictionaries in search params to be serialized
        if request.params:
            for k, v in request.params.items():
                if isinstance(v, dict):
                    # Compact json - omit the '+' values for spaces, otherwise API breaks
                    request.params[k] = json.dumps(v, separators=(',', ':'))

        if request.requires_token:
            if method in [HTTPMethod.GET, HTTPMethod.DELETE]:  # Add token to url
                request.params = {
                    **(request.params or {}),
                    'token': self.get_token()
                }
            elif method in [HTTPMethod.POST, HTTPMethod.PUT]:  # Add token to body
                request.json = {
                    **(request.json or {}),
                    'token': self.get_token(),
                }
                # Add token to `data` only if it exists
                if request.data:
                    request.data = {
                        **request.data,
                        'token': self.get_token(),
                    }
