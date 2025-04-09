from enum import StrEnum

ResponseData = str | bytes | dict


class ResponseDtype(StrEnum):
    TEXT = 'text'
    BINARY = 'binary'
    JSON = 'json'
