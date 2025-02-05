import importlib
import inspect
import pkgutil

from pyguru import endpoints
from pyguru.adapter import LabguruAdapter
from pyguru.credentials.credentials import Credentials


class PyGuru:

    def __init__(self, username: str = None, password: str = None) -> None:
        # self.register_endpoints()
        self.adapter = LabguruAdapter(credentials=Credentials(username, password))

        def register_endpoint(self, module_info):
            # TODO change endpoints
            module = importlib.import_module(f'endpoints.{module_info.name}')
            for _, cls in inspect.getmembers(module, inspect.isclass):
                if cls.__module__ == module.__name__:
                    setattr(self, module_info.name, cls(self.adapter))

        def register_endpoints(self, endpoints_path: str):
            for module_info in pkgutil.iter_modules(endpoints_path):
                self.register_endpoint(module_info)


pyguru = PyGuru()
print(pyguru.adapter.get_token())
