from typing import Literal, Any, Callable
from ._utils import message_to_str


def make_log_method(user_level: Literal[0, 1, 2, 3, 4]) -> Callable[[Any, bool, Exception], None]:
    """
    Factory function that creates a logging method for a specific log level.

    Args:
        user_level (Literal[0, 1, 2, 3, 4]): The severity level for the log method.
            0 = DEBUG, 1 = INFO, 2 = WARNING, 3 = ERROR, 4 = CRITICAL (or raise exception)

    Returns:
        Callable: A function that can be used as a logging method in a logger class.
    """

    def log_method(self, *message: Any, additional_info: bool = True, **kwargs) -> None:
        """
        Log a message if the logger's level allows it. Optionally raises an exception
        if the log level is critical.

        Args:
            self (Logger): The logger instance.
            *message (Any): One or more objects to be logged.
            additional_info (bool, optional): If True, adds extra context such as
                timestamp or caller name. Defaults to True.
            **kwargs: Optional keyword arguments.
                - exception_type (Type[Exception], optional): The exception class to raise
                  if user_level == 4. Defaults to Exception.

        Raises:
            Exception: If user_level == 4 and 'exception_type' is specified in kwargs.
        """
        if user_level >= self._logger_level:
            caller_name = self._get_caller_name()
            message = message_to_str(*message)

            self._send(
                message,
                caller_name=caller_name,
                additional_info=additional_info,
                now_log_level=user_level,
            )

            if user_level == 4:
                exception_type = kwargs.get("exception_type", Exception)
                raise exception_type(message)

    return log_method
