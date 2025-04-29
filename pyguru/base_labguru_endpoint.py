from __future__ import annotations

from typing import TYPE_CHECKING, Generator

from pyguru.request.request import Request
from pyguru.request.response_dtype import ResponseDtype

if TYPE_CHECKING:
    from pyguru.adapter import LabguruAdapter
    from pyguru.request.response_dtype import ResponseData


class BaseLabguruEndpoint:

    def __init__(self, adapter: LabguruAdapter, route: str) -> None:
        self.adapter = adapter
        self.route = route

    def _get_full_endpoint(self,  resource_id: int | None = None, sub_route: str | None = None) -> str:
        route = self.route
        for url_component in [resource_id, sub_route]:  # Order matters
            if url_component is not None:
                route += f'/{url_component}'
        return route

    def get_by_id(self, resource_id: int):
        request = Request(endpoint=f'{self.route}/{resource_id}')
        _, resp_data = self.adapter.get(request)
        return resp_data

    def get(
        self,
        sub_route: str | None = None,
        params: dict[str, str] | None = None,
        response_dtype: ResponseDtype = ResponseDtype.JSON
    ):
        request = Request(
            endpoint=self._get_full_endpoint(sub_route=sub_route),
            params=params,
            response_dtype=response_dtype
        )
        _, resp_data = self.adapter.get(request)
        return resp_data

    def paginate(
        self,
        sub_route: str | None = None,
        params: dict[str, str] | None = None,
    ) -> Generator[int, ResponseData]:
        # if page exists in the search parameters, remove it as this iterates over the pages
        params = params or {}
        while (resp := self.get(sub_route=sub_route, params=params)):
            # If `meta` is included, the response is divided into `meta` containing paging information,
            # and `data` for the actual result
            # otherwise, if `meta` is False (as it is by default), the response consists only of the data
            if params.get('meta', False) and not resp.get('data', []):
                break
            yield params['page'], resp
            params['page'] += 1

    def post(
        self,
        sub_route: str | None = None,
        json_data: dict | None = None,
        data: dict[str, str] | None = None,
        files: list[str] | None = None
    ):
        request = Request(
            endpoint=self._get_full_endpoint(sub_route=sub_route),
            json=json_data,
            data=data,
            files=files
        )
        _, resp_data = self.adapter.post(request)
        return resp_data

    def put(self, resource_id: int, json_data: dict, sub_route: str | None = None):
        request = Request(
            endpoint=self._get_full_endpoint(resource_id=resource_id, sub_route=sub_route),
            json=json_data
        )
        _, resp_data = self.adapter.put(request)
        return resp_data

    def delete(self, resource_id: int):
        request = Request(endpoint=self._get_full_endpoint(resource_id=resource_id))
        _, resp_data = self.adapter.delete(request)
        return resp_data
