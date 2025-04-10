from datetime import datetime

from rich.console import Console
from rich.text import Text

from ten_utils.common.constants import (
    LOGGER_LEVELS,
    LOGGER_INFO,
    LOGGER_FORMAT,
    CONSOLE_THEME,
)
from ten_utils.common.decorators import check_now_log_level
from ten_utils.log.config import LoggerConfig


class Logger:
    """
    Logger class for structured, colorized logging with configurable log levels,
    optional file persistence, and named logger instances.

    This logger supports five standard logging levels:
        0 - DEBUG
        1 - INFO
        2 - WARNING
        3 - ERROR
        4 - CRITICAL

    The logger level and file output behavior can be configured globally
    using the LoggerConfig singleton, or overridden per instance.

    Attributes:
        name (str | None): Custom name for the logger (e.g., module or class name).
        level (int): Minimum level to log (messages below this level are ignored).
        save_file (bool): Flag indicating whether logs should be written to a file.
        console (Console): Rich console instance for stylized output.
    """

    logger_level = LOGGER_INFO  # Default logging level set to INFO

    def __init__(
        self,
        name: str | None = None,
        level: int | None = None,
        save_file: bool | None = None,
    ):
        """
        Initializes a Logger instance, with optional overrides for log level and file saving.

        If level and save_file are not specified, global defaults are taken from LoggerConfig.

        Args:
            name (str | None): Identifier shown in the log output. Useful for filtering by source.
            level (int | None): Minimum level of logs to show. Defaults to LoggerConfig setting.
            save_file (bool | None): If True, logs will also be written to file. Defaults to LoggerConfig setting.
        """
        logger_config = LoggerConfig()

        self.name = name
        self.level = level if level is not None else logger_config.get_default_level_log()
        self.save_file = save_file if save_file is not None else logger_config.get_save_log_to_file()
        self.console = Console(theme=CONSOLE_THEME)

    def __send(
            self,
            message: str,
            name: str,
            now_log_level: int,
            additional_info: bool,
    ) -> None:
        """
        Internal method to format and dispatch log messages to the console and optionally to file.

        Args:
            message (str): The log message content.
            name (str): A tag or source name (e.g., function or component).
            now_log_level (int): The numeric level of the log (0–4).
            additional_info (bool): Flag to indicate whether to include full logging information
                (including date, time, level, logger name, and source).

        Returns:
            None

        Side Effects:
            Outputs the message to console.
            (Future) Appends to log file if save_file is True.
        """
        # Format log message with current timestamp
        arg_string = (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            LOGGER_LEVELS[now_log_level].upper(),
            self.name,
            name,
            message,
        )

        # Conditionally adjust log format based on whether additional info is requested
        if not additional_info:
            logger_format = LOGGER_FORMAT.split(":")[1].strip(" ")
        else:
            logger_format = LOGGER_FORMAT

        message = logger_format.format(*arg_string)
        level_style = LOGGER_LEVELS.get(now_log_level, "info")

        # Print the message using Rich's styled console output
        self.console.print(Text(text=message, style=level_style))

        # Optional file output (future implementation)
        if self.save_file:
            pass

    @check_now_log_level(user_level=0)
    def debug(
            self,
            message: str,
            name: str | None = None,
            additional_info: bool = True,
    ) -> None:
        """
        Logs a debug message. Typically used for development and low-level system info.

        Args:
            message (str): Debug information to log.
            name (str): Context (e.g., method name or identifier) generating the log.
            additional_info (bool, optional): If True, logs will include timestamp, log level,
                logger name, and source. Defaults to True.

        Returns:
            None
        """
        self.__send(
            message,
            name,
            0,  # DEBUG level
            additional_info,
        )

    @check_now_log_level(user_level=1)
    def info(
            self,
            message: str,
            name: str | None = None,
            additional_info: bool = True,
    ) -> None:
        """
        Logs an informational message about normal operations.

        Args:
            message (str): Informational text.
            name (str, optional): Optional source/context name.
            additional_info (bool, optional): If True, logs will include timestamp, log level,
                logger name, and source. Defaults to True.

        Returns:
            None
        """
        self.__send(
            message,
            name,
            1,  # INFO level
            additional_info,
        )

    @check_now_log_level(user_level=2)
    def warning(
            self,
            message: str,
            name: str | None = None,
            additional_info: bool = True,
    ) -> None:
        """
        Logs a warning message that indicates a potential problem.

        Args:
            message (str): Warning text.
            name (str, optional): Optional context source.
            additional_info (bool, optional): If True, logs will include timestamp, log level,
                logger name, and source. Defaults to True.

        Returns:
            None
        """
        self.__send(
            message,
            name,
            2,  # WARNING level
            additional_info,
        )

    @check_now_log_level(user_level=3)
    def error(
            self,
            message: str,
            name: str | None = None,
            additional_info: bool = True,
    ) -> None:
        """
        Logs an error message indicating a failure in processing.

        Args:
            message (str): Error description.
            name (str, optional): Context of the error.
            additional_info (bool, optional): If True, logs will include timestamp, log level,
                logger name, and source. Defaults to True.

        Returns:
            None
        """
        self.__send(
            message,
            name,
            3,  # ERROR level
            additional_info,
        )

    @check_now_log_level(user_level=4)
    def critical(
            self,
            message: str,
            name: str | None = None,
            additional_info: bool = True,
    ) -> None:
        """
        Logs a critical error that may result in application termination.

        Args:
            message (str): Critical error text.
            name (str, optional): Optional context (e.g., function name).
            additional_info (bool, optional): If True, logs will include timestamp, log level,
                logger name, and source. Defaults to True.

        Returns:
            None

        Side Effects:
            Exits the program with code 1.
        """
        self.__send(
            message,
            name,
            4,  # CRITICAL level
            additional_info,
        )
        exit(1)
