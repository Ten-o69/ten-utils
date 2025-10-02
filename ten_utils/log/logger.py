from datetime import datetime
from typing import Literal
import inspect

from rich.console import Console
from rich.text import Text

from .._common import (
    LOGGER_LEVELS,
    LOGGER_INFO,
    LOGGER_FORMAT,
    CONSOLE_THEME,
)
from ._factory import make_log_method


class Logger:
    """
    A structured and stylized logger supporting colored console output and log level filtering.

    The Logger provides five logging levels:
        0 - DEBUG
        1 - INFO
        2 - WARNING
        3 - ERROR
        4 - CRITICAL

    Attributes:
        name (str | None): Optional identifier for the logger (e.g., module or class name).
        level (int): Minimum log level to display; messages below this level will be ignored.
        save_file (bool | None): Whether to persist log messages to a file (currently not implemented).
        console (Console): Rich Console instance used to print styled messages to the terminal.
    """

    def __init__(
        self,
        name: str | None = None,
        level: Literal[0, 1, 2, 3, 4] = LOGGER_INFO,
        save_file: bool | None = None,
    ):
        """
        Initialize a new Logger instance with optional overrides for logging level and file saving behavior.

        Args:
            name (str | None): Optional label used to tag log output (e.g., a class or module name).
            level (Literal[0, 1, 2, 3, 4]): Minimum severity level to log. Defaults to INFO.
            save_file (bool | None): Whether to save logs to a file. Defaults to None.
        """
        self.name = name
        self.level = level
        self.save_file = save_file
        self.console = Console(theme=CONSOLE_THEME)

    @staticmethod
    def _get_caller_name() -> str:
        """
        Retrieve the name of the caller function or method.

        Returns:
            str: The name of the function or method that called the logger.
        """
        frame = inspect.currentframe()
        caller_frame = frame.f_back.f_back

        return caller_frame.f_code.co_name

    def _send(
            self,
            message: str,
            caller_name: str,
            now_log_level: int,
            additional_info: bool,
    ) -> None:
        """
        Format and output a log message to the console, and optionally to a file.

        Args:
            message (str): The log message content.
            caller_name (str): Context or identifier of the log message source.
            now_log_level (int): Numeric representation of the log level (0 to 4).
            additional_info (bool): Whether to include timestamp, log level, logger name, and source in output.

        Side Effects:
            Prints the log message to the console.
            (Future) Writes the log message to a file if `save_file` is True.
        """
        arg_string = (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            LOGGER_LEVELS[now_log_level].upper(),
            self.name,
            caller_name,
            message,
        )

        logger_format = (
            LOGGER_FORMAT if additional_info else LOGGER_FORMAT.split(":")[1].strip(" ")
        )

        message = logger_format.format(*arg_string)
        level_style = LOGGER_LEVELS.get(now_log_level, "info")

        self.console.print(Text(text=message, style=level_style))

        if self.save_file:
            pass  # Placeholder for future file writing implementation

    debug = make_log_method(0)
    info = make_log_method(1)
    warning = make_log_method(2)
    error = make_log_method(3)
    critical = make_log_method(4)
