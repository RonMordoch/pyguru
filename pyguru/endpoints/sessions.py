from pyguru.base_labguru_endpoint import BaseLabguruEndpoint
from pyguru.request.request import Request


class SessionsEndpoint(BaseLabguruEndpoint):

    def __init__(self, adapter) -> None:
        super().__init__(adapter, 'sessions')

    def get_token(self, username: str, password: str, account_id: int | None = None):
        login_data = {
            'login': username,
            'password': password
        }
        if account_id is not None:
            login_data['account_id'] = account_id
        request = Request(
            endpoint=self.route,
            json=login_data,
            requires_token=False
        )
        _, resp_data = self.adapter.post(request)
        return resp_data['token']
