from http import HTTPMethod, HTTPStatus

import requests

from pyguru.adapter import ResponseData, ResponseDtype


class RestAdapter:

    @staticmethod
    def get_api_fqdn(host: str, version: str) -> str:
        return f'https://{host}/{version}'

    @staticmethod
    def is_response_ok(resp: requests.Response) -> bool:
        return (HTTPStatus.OK <= resp.status_code < HTTPStatus.MULTIPLE_CHOICES)

    # TODO return type
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

    def _request(
        self,
        method: HTTPMethod,
        endpoint: str,
        response_dtype: ResponseDtype,
        headers: dict[str, str] | None = None,
        params: dict[str, str] | None = None,
        json: dict[str, str] | None = None,
        data: dict[str, str] | None = None,
        files=None,
        timeout: float | tuple | None = None
    ) -> tuple[HTTPStatus, ResponseData]:
        url = f'{self.api_url}/{endpoint}'
        resp = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            data=data,
            json=json,
            files=files,
            timeout=timeout
        )
        resp_data = self.parse_response(resp, response_dtype)
        if self.is_response_ok(resp):
            return HTTPStatus(resp.status_code), resp_data
        raise Exception(resp_data['message'])  # TODO Decide on custom exception or return class

    def get(
        self,
        endpoint: str,
        response_dtype: ResponseDtype = ResponseDtype.JSON,
        headers: dict[str, str] | None = None,
        params: dict[str, str] | None = None,
        timeout: float | tuple | None = None
    ) -> tuple[HTTPStatus, ResponseData]:
        return self._request(
            method=HTTPMethod.GET,
            endpoint=endpoint,
            response_dtype=response_dtype,
            headers=headers,
            params=params,
            timeout=timeout
        )

    def post(
        self,
        endpoint: str,
        response_dtype: ResponseDtype = ResponseDtype.JSON,
        headers: dict[str, str] | None = None,
        params: dict[str, str] | None = None,
        json: dict[str, str] | None = None,
        data: dict[str, str] | None = None,
        files=None,
        timeout: float | tuple | None = None
    ) -> tuple[HTTPStatus, ResponseData]:
        return self._request(
            method=HTTPMethod.POST,
            endpoint=endpoint,
            response_dtype=response_dtype,
            headers=headers,
            params=params,
            json=json,
            data=data,
            files=files,
            timeout=timeout
        )

    def put(
        self,
        endpoint: str,
        response_dtype: ResponseDtype = ResponseDtype.JSON,
        headers: dict[str, str] | None = None,
        params: dict[str, str] | None = None,
        json: dict[str, str] | None = None,
        data: dict[str, str] | None = None,
        files=None,
        timeout: float | tuple | None = None
    ) -> tuple[HTTPStatus, ResponseData]:
        return self._request(
            method=HTTPMethod.DELETE,
            endpoint=endpoint,
            response_dtype=response_dtype,
            headers=headers,
            params=params,
            json=json,
            data=data,
            timeout=timeout
        )
