from pathlib import Path
from typing import Any
import os

from dotenv import load_dotenv

from ten_utils.common.validators import EnvLoaderValuesValidator
from ten_utils.common.errors import (
    FailedLoadEnvVariables,
    FailedConvertTypeEnvVar,
    NotFoundNameEnvVar,
)
from ten_utils.common.singleton import Singleton


class EnvLoader(metaclass=Singleton):
    def __init__(self, path_to_env_file: str | Path):
        loader_env_values = EnvLoaderValuesValidator(
            path_to_env_file=path_to_env_file,
        )

        self.path_to_env_file = loader_env_values.path_to_env_file
        load_result: bool = load_dotenv(dotenv_path=self.path_to_env_file)

        if not load_result:
            raise FailedLoadEnvVariables

    def load(self, name_env: str, type_env_var: type) -> Any:
        env_value: str | None = os.getenv(name_env)
        if env_value is None:
            raise NotFoundNameEnvVar(name_env=name_env)

        if type_env_var is None:
            raise ValueError(
                "The 'type_env_var' argument cannot be 'None'"
            )

        elif type_env_var is list or type_env_var is tuple:
            return self.__convert_var_to_list_or_tuple(
                env_value=env_value,
                type_env_var=type_env_var,
            )

        try:
            return type_env_var(env_value)

        except ValueError:
            raise FailedConvertTypeEnvVar(
                convert_type=type_env_var,
                value=env_value,
            )

    @staticmethod
    def __convert_var_to_list_or_tuple(
            env_value: str,
            type_env_var: type,
    ) -> list | tuple:
        env_value = env_value.split(",")

        for key, value in enumerate(env_value):
            if value == "":
                del env_value[key]

        if type_env_var is tuple:
            return tuple(env_value)

        return env_value
