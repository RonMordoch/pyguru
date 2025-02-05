from .base_labguru_endpoint import BaseLabguruEndpoint


class AuthEndpoint(BaseLabguruEndpoint):

    def __init__(self, adapter) -> None:
        super().__init__(adapter)

    def get_token(self, username: str, password: str):
        _, resp_data = self.adapter.post(
            'sessions',
            json={
                'login': username,
                'password': password
            }
        )
        return resp_data['token']
