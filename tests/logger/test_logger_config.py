import pytest
from ten_utils.log.config import LoggerConfig


def test_singleton_instance():
    config1 = LoggerConfig()
    config2 = LoggerConfig()
    assert config1 is config2


def test_default_level_log():
    config = LoggerConfig()
    assert config.get_default_level_log() == 1

    config.set_default_level_log(3)
    assert config.get_default_level_log() == 3


def test_invalid_level_log():
    config = LoggerConfig()
    config.set_default_level_log(5)  # invalid level
    assert config.get_default_level_log() == 1


def test_save_log_to_file_flag():
    config = LoggerConfig()
    assert config.get_save_log_to_file() is False

    config.set_save_log_to_file(True)
    assert config.get_save_log_to_file() is True


def test_invalid_save_log_to_file():
    config = LoggerConfig()
    config.set_save_log_to_file("yes")  # not a boolean
    assert config.get_save_log_to_file() is False
