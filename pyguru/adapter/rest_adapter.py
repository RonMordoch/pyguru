from http import HTTPMethod, HTTPStatus

import requests

from pyguru.request.request import Request
from pyguru.request.response_dtype import ResponseData, ResponseDtype


class RestAdapter:

    @staticmethod
    def get_api_fqdn(host: str, version: str) -> str:
        return f'https://{host}/{version}'

    @staticmethod
    def is_response_ok(resp: requests.Response) -> bool:
        return (HTTPStatus.OK <= resp.status_code < HTTPStatus.MULTIPLE_CHOICES)

    @staticmethod
    def parse_response(resp: requests.Response, response_dtype: ResponseDtype) -> ResponseData:
        match response_dtype:
            case ResponseDtype.TEXT:
                return resp.text
            case ResponseDtype.BINARY:
                return resp.content
            case ResponseDtype.JSON | _:
                return resp.json()

    def __init__(self, host: str, version: str) -> None:
        self.api_url = self.get_api_fqdn(host, version)

    def pre_request_hook(self, method: HTTPMethod, request: Request):
        pass

    def post_request_hook(self, method: HTTPMethod, request: Request):
        pass

    def _request(
        self,
        method: HTTPMethod,
        request: Request
    ) -> tuple[HTTPStatus, ResponseData]:
        url = f'{self.api_url}/{request.endpoint}'
        self.pre_request_hook(method, request)
        resp = requests.request(
            method=method,
            url=url,
            headers=request.headers,
            params=request.params,
            data=request.data,
            json=request.json,
            files=request.files,
            timeout=request.timeout
        )
        self.post_request_hook(method, request)
        resp_data = self.parse_response(resp, request.response_dtype)
        if self.is_response_ok(resp):
            return HTTPStatus(resp.status_code), resp_data
        raise Exception(resp_data['message'])  # TODO Decide on custom exception or return class

    def get(self, request: Request) -> tuple[HTTPStatus, ResponseData]:
        return self._request(method=HTTPMethod.GET, request=request)

    def post(self, request: Request) -> tuple[HTTPStatus, ResponseData]:
        return self._request(method=HTTPMethod.POST, request=request)

    def put(self, request: Request) -> tuple[HTTPStatus, ResponseData]:
        return self._request(method=HTTPMethod.PUT, request=request)

    def delete(self, request: Request) -> tuple[HTTPStatus, ResponseData]:
        return self._request(method=HTTPMethod.DELETE, request=request)
