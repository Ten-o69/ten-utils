from typing import Any


def message_to_str(*message: Any) -> str:
    """
    Convert multiple input values to a single string suitable for logging.

    Args:
        *message (Any): One or more values of any type to be converted to string.

    Returns:
        str: A single string where all input values are concatenated with spaces.

    Example:
        >>> message_to_str("Error code:", 404, "occurred")
        'Error code: 404 occurred'
    """

    return " ".join(str(i) for i in message)