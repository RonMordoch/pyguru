from pyguru.base_labguru_endpoint import BaseLabguruEndpoint


class WebhooksEndpoint(BaseLabguruEndpoint):

    def __init__(self, adapter) -> None:
        super().__init__(adapter, 'webhooks')

    def list(self):
        return self.get(sub_route='list')
