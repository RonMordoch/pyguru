from dataclasses import dataclass

from .response_dtype import ResponseDtype


@dataclass
class Request:
    endpoint: str
    response_dtype: ResponseDtype = ResponseDtype.JSON
    headers: dict[str, str] | None = None
    params: dict[str, str] | None = None
    json: dict[str, str] | None = None
    data: dict[str, str] | None = None
    files: list[str] | None = None  # TODO annotation
    timeout: float | None = None
    requires_token: bool = True
