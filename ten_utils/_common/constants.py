from rich.theme import Theme


# logger
LOGGER_DEBUG = 0
LOGGER_INFO = 1
LOGGER_WARNING = 2
LOGGER_ERROR = 3
LOGGER_CRITICAL = 4
LOGGER_LEVELS = {
    LOGGER_DEBUG: "debug",
    LOGGER_INFO: "info",
    LOGGER_WARNING: "warning",
    LOGGER_ERROR: "error",
    LOGGER_CRITICAL: "critical"
}
LOGGER_FORMAT = "{0} [{1}] {2}.{3}: {4}"

# rich
CONSOLE_THEME = Theme({
    "debug": "white",
    "info": "cyan",
    "warning": "yellow",
    "error": "red",
    "critical": "bold red",
})
