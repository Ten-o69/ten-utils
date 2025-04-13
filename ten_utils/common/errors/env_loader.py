from typing import Any

from .base import TenUtilsLibError


class FailedLoadEnvVariables(TenUtilsLibError):
    def __init__(self):
        super().__init__(
            "Not a single environment variable was loaded. "
            "Either the file with environment variables was "
            "not found or the file with environment variables is empty."
        )


class FailedConvertTypeEnvVar(TenUtilsLibError):
    def __init__(self, convert_type: type, value: Any):
        super().__init__(
            f"Converting an environment variable to type {convert_type!r} failed. "
            f"Most likely the value {value!r} cannot be converted to {convert_type!r} type."
        )


class NotFoundNameEnvVar(TenUtilsLibError):
    def __init__(self, name_env: str):
        super().__init__(
            f"The environment variable name {name_env!r} was not found."
        )
