from pyguru.base_labguru_endpoint import BaseLabguruEndpoint


class MaintenanceEventsEndpoint(BaseLabguruEndpoint):

    def __init__(self, adapter) -> None:
        super().__init__(adapter, 'maintenance_events')
