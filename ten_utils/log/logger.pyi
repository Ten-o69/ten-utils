from typing import Any, Literal, Type

from rich.console import Console

from .._common import CONSOLE_THEME

class Logger:
    def __init__(
        self,
        name: str | None = None,
        save_file: bool | None = None,
    ):
        self.name = name
        self.save_file = save_file
        self.console = Console(theme=CONSOLE_THEME)

    _logger_level: Literal[0, 1, 2, 3, 4] = ...

    def debug(self, *message: Any, additional_info: bool = True, **kwargs) -> None:
        """
        Log a message at DEBUG level (0).

        This level is intended for diagnostic output useful during development,
        such as variable values, execution flow, or internal states.

        Args:
            *message (Any): One or more objects to be logged.
            additional_info (bool, optional): If True, includes timestamp, log level,
                logger name, and caller name. Defaults to True.
            **kwargs: Additional keyword arguments (not commonly used at this level).
        """

    def info(self, *message: Any, additional_info: bool = True, **kwargs) -> None:
        """
        Log a message at INFO level (1).

        This level is intended for general informational messages that highlight
        the progress of the application at a coarse-grained level.

        Args:
            *message (Any): One or more objects to be logged.
            additional_info (bool, optional): If True, includes timestamp, log level,
                logger name, and caller name. Defaults to True.
            **kwargs: Additional keyword arguments (not commonly used at this level).
        """

    def warning(self, *message: Any, additional_info: bool = True, **kwargs) -> None:
        """
        Log a message at WARNING level (2).

        This level indicates potentially harmful situations that are not
        necessarily errors but might require attention.

        Args:
            *message (Any): One or more objects to be logged.
            additional_info (bool, optional): If True, includes timestamp, log level,
                logger name, and caller name. Defaults to True.
            **kwargs: Additional keyword arguments (not commonly used at this level).
        """

    def error(self, *message: Any, additional_info: bool = True) -> None:
        """
        Log a message at ERROR level (3).

        This level indicates that an error has occurred, typically one that
        prevents normal execution of part of the application but does not
        stop the whole program.

        Args:
            *message (Any): One or more objects to be logged.
            additional_info (bool, optional): If True, includes timestamp, log level,
                logger name, and caller name. Defaults to True.
        """

    def critical(
            self,
            *message: Any,
            additional_info: bool = True,
            exception_type: Type[Exception] = Exception,
    ) -> None:
        """
        Log a message at CRITICAL level (4).

        This level indicates a severe error that may cause the application
        to terminate. By default, it also raises an exception after logging.

        Args:
            *message (Any): One or more objects to be logged.
            additional_info (bool, optional): If True, includes timestamp, log level,
                logger name, and caller name. Defaults to True.
            exception_type (Type[Exception], optional): The exception class to raise
                after logging. Defaults to Exception.

        Raises:
            Exception: Always raised after logging unless overridden by exception_type.
        """

    def _send(
            self,
            message: str,
            caller_name: str,
            now_log_level: Literal[0, 1, 2, 3, 4],
            additional_info: bool,
    ) -> None: ...
    @staticmethod
    def _get_caller_name() -> str: ...

    @classmethod
    def set_logger_level(cls, level: Literal[0, 1, 2, 3, 4]) -> None: ...
    @classmethod
    def get_logger_level(cls) -> Literal[0, 1, 2, 3, 4]: ...
