from typing import Any

from .singleton import Singleton


class Buffer(metaclass=Singleton):
    def __init__(self):
        self.__buffer: dict[str, Any] = {}

    def set(self, key: str, value: Any):
        self.__buffer[key] = value

    def get(self, key: str):
        return self.__buffer.get(key)

    def clear(self):
        self.__buffer = {}
