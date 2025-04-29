import importlib
import inspect
import pkgutil
from pathlib import Path

from pyguru import endpoints
from pyguru.adapter import LabguruAdapter
from pyguru.base_labguru_endpoint import BaseLabguruEndpoint
from pyguru.credentials.credentials import Credentials, CredentialsFile


class PyGuru:

    GENERIC_ENDPOINTS = [BaseLabguruEndpoint, endpoints.BiocollectionsEndpoint]

    def __init__(
        self,
        username: str = None,
        password: str = None,
        profile_name: str = CredentialsFile.DEFAULT_PROFILE_NAME,
        host=LabguruAdapter.HOST
    ) -> None:
        self.credentials = Credentials(username, password, host=host, profile_name=profile_name)
        self.adapter = LabguruAdapter(
            credentials=self.credentials,
            host=self.credentials.data.host or host
        )
        # Explicitly register endpoints for better IDE support
        self.antibodies = endpoints.AntibodiesEndpoint(self.adapter)
        self.bacteria = endpoints.BacteriaEndpoint(self.adapter)
        self.boxes = endpoints.BoxesEndpoint(self.adapter)
        self.cell_lines = endpoints.CellLinesEndpoint(self.adapter)
        self.comments = endpoints.CommentsEndpoint(self.adapter)
        self.companies = endpoints.CompaniesEndpoint(self.adapter)
        self.compounds = endpoints.CompoundsEndpoint(self.adapter)
        self.datasets = endpoints.DatasetsEndpoint(self.adapter)
        self.documents = endpoints.DocumentsEndpoint(self.adapter)
        self.experiments = endpoints.ExperimentsEndpoint(self.adapter)
        self.flies = endpoints.FliesEndpoint(self.adapter)
        self.folders = endpoints.FoldersEndpoint(self.adapter)
        self.fungi = endpoints.FungiEndpoint(self.adapter)
        self.genes = endpoints.GenesEndpoint(self.adapter)
        self.lipids = endpoints.LipidsEndpoint(self.adapter)
        self.plants = endpoints.PlantsEndpoint(self.adapter)
        self.projects = endpoints.ProjectsEndpoint(self.adapter)
        self.proteins = endpoints.ProteinsEndpoint(self.adapter)
        self.protocols = endpoints.ProtocolsEndpoint(self.adapter)
        self.reports = endpoints.ReportsEndpoint(self.adapter)
        self.sequences = endpoints.SequencesEndpoint(self.adapter)
        self.sessions = endpoints.SessionsEndpoint(self.adapter)
        self.shopping_list = endpoints.ShoppingListEndpoint(self.adapter)
        self.sops = endpoints.SopsEndpoint(self.adapter)
        self.stocks = endpoints.StocksEndpoint(self.adapter)
        self.storages = endpoints.StoragesEndpoint(self.adapter)
        self.tags = endpoints.TagsEndpoint(self.adapter)
        self.teams = endpoints.TeamsEndpoint(self.adapter)
        self.tissues = endpoints.TissuesEndpoint(self.adapter)
        self.units = endpoints.UnitsEndpoint(self.adapter)
        self.vectors = endpoints.VectorsEndpoint(self.adapter)
        self.viruses = endpoints.VirusesEndpoint(self.adapter)
        self.visualizations = endpoints.VisualizationsEndpoint(self.adapter)
        self.webhooks = endpoints.WebhooksEndpoint(self.adapter)
        self.worms = endpoints.WormsEndpoint(self.adapter)
        self.yeasts = endpoints.YeastsEndpoint(self.adapter)
        # Register any additional endpoints dynamically
        self.register_endpoints(str(Path(__file__).parent / 'endpoints'))

    def register_endpoint_cls(self, module_name: str, endpoint_cls: BaseLabguruEndpoint):
        setattr(self, module_name, endpoint_cls(self.adapter))

    def register_endpoint(self, module_info):
        module = importlib.import_module(f'pyguru.endpoints.{module_info.name}')
        for _, cls in inspect.getmembers(module, inspect.isclass):
            if cls in self.GENERIC_ENDPOINTS:
                continue
            if cls.__module__ == module.__name__ and not hasattr(self, module_info.name):
                setattr(self, module_info.name, cls(self.adapter))

    def register_endpoints(self, endpoints_path: str):
        for module_info in pkgutil.iter_modules([endpoints_path]):
            self.register_endpoint(module_info)
