
from pyguru.base_labguru_endpoint import BaseLabguruEndpoint
from pyguru.request.response_dtype import ResponseDtype


class AttachmentsEndpoint(BaseLabguruEndpoint):

    def __init__(self, adapter) -> None:
        super().__init__(adapter, 'attachments')

    def download(self, attachment_id: int):
        """
        Inferred from working with the API, route is not documented in official docs as of April 2025.
        """
        return self.get(sub_route=f'{attachment_id}/download', response_dtype=ResponseDtype.BINARY)
