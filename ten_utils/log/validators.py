from typing import Any, Literal

from ten_utils.common.constants import LOGGER_LEVELS


def validate_value_default_level_log(value: Any) -> Literal[0, 1, 2, 3, 4]:
    """
    Validates the input value to determine if it is a valid logger level.

    Args:
        value (Any): Input value to be validated.

    Returns:
        Literal[0, 1, 2, 3, 4]: The validated logger level.
        If the input is invalid, returns the default level `1` (INFO).

    Notes:
        - Acceptable values must be among the keys of LOGGER_LEVELS.
        - Falls back to default log level 1 if invalid input is provided.
    """
    if value not in LOGGER_LEVELS.keys():
        return 1

    return value


def validate_value_save_log_to_file(value: Any) -> bool:
    """
    Validates whether the given value is a boolean.

    Args:
        value (Any): Input value to be validated.

    Returns:
        bool: `True` or `False` if the value is a boolean.
              Returns `False` for any non-boolean input.

    Notes:
        - This validator ensures only boolean values are accepted.
        - Falls back to `False` if the type is invalid.
    """
    if not isinstance(value, bool):
        return False

    return value
