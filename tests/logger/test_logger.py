import pytest
from unittest.mock import patch
from ten_utils.log.logger import Logger


@pytest.fixture
def mock_console_print():
    """
    Fixture that patches `rich.Console.print` to isolate output during tests.

    This prevents actual console output and allows verification of whether
    the `Logger` attempted to print messages.
    """
    with patch("ten_utils.log.logger.Console.print") as mock_print:
        yield mock_print


@pytest.fixture
def logger():
    """
    Fixture that creates a basic `Logger` instance for testing.

    Returns:
        Logger: A configured logger instance with console output only.
    """
    return Logger(name="TestLogger", save_file=False)


@pytest.mark.parametrize(
    "method,level,should_log",
    [
        ("debug", "DEBUG", False),
        ("info", "INFO", True),
        ("warning", "WARNING", True),
        ("error", "ERROR", True),
        ("critical", "CRITICAL", True),
    ],
)
def test_log_output_contains_expected_parts(logger, mock_console_print, method, level, should_log):
    """
    Verify that each logging level produces expected output or is correctly skipped.

    The test dynamically calls each log method (debug, info, etc.) and inspects
    whether the output contains the correct log level, logger name, and message text.
    Critical logs are also expected to raise exceptions.
    """
    log_method = getattr(logger, method)

    if method == "critical":
        with pytest.raises(Exception):
            log_method("Test message")
    else:
        log_method("Test message")

    if should_log:
        assert mock_console_print.called, f"{method} should have triggered print()"
        text_obj = mock_console_print.call_args[0][0]
        output = text_obj.plain
        assert "Test message" in output
        assert level in output
        assert "TestLogger" in output
    else:
        assert not mock_console_print.called, f"{method} should not have triggered print()"


def test_log_without_additional_info(logger, mock_console_print):
    """
    Verify that when `additional_info=False`, only the raw message is displayed.

    The output should not include metadata such as log level, logger name, or timestamp.
    """
    logger.info("Short message", additional_info=False)

    text_obj = mock_console_print.call_args[0][0]
    output = text_obj.plain

    assert "INFO" not in output
    assert "TestLogger" not in output
    assert "Short message" in output


def test_logger_level_set_and_get():
    """
    Ensure that class-level logger configuration methods work correctly.

    Tests both `Logger.set_logger_level` and `Logger.get_logger_level`
    for proper state management.
    """
    Logger.set_logger_level(3)
    assert Logger.get_logger_level() == 3

    Logger.set_logger_level(1)
    assert Logger.get_logger_level() == 1


def test_critical_raises_specified_exception(logger, mock_console_print):
    """
    Ensure that `Logger.critical` raises the specified exception type.

    The method should both log the message at CRITICAL level and raise
    the exception class provided via the `exception_type` argument.
    """
    with pytest.raises(AttributeError):
        logger.critical("Fatal issue", exception_type=AttributeError)

    assert mock_console_print.called
    output = mock_console_print.call_args[0][0].plain
    assert "CRITICAL" in output
    assert "Fatal issue" in output
