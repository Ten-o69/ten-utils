from pathlib import Path

from pydantic import BaseModel, field_validator


class EnvLoaderValuesValidator(BaseModel):
    path_to_env_file: str | Path

    @field_validator("path_to_env_file")
    def check_path_to_env_file(cls, value) -> Path:
        if isinstance(value, str):
            return Path(value)

        return value
