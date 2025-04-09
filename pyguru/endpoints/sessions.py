from pyguru.base_labguru_endpoint import BaseLabguruEndpoint
from pyguru.request.request import Request


class SessionsEndpoint(BaseLabguruEndpoint):

    def __init__(self, adapter) -> None:
        super().__init__(adapter, 'sessions')

    def get_token(self, username: str, password: str):
        request = Request(
            endpoint=self.route,
            json={
                'login': username,
                'password': password
            },
            requires_token=False
        )
        _, resp_data = self.adapter.post(request)
        return resp_data['token']
