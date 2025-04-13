from typing import Literal

from pydantic import BaseModel


class LoggerConfigValidator(BaseModel):
    default_level_log: Literal[0, 1, 2, 3, 4]
    save_log_to_file: bool
