from typing import Any, Literal, Type

class Logger:
    def __init__(
        self,
        name: str | None = None,
        level: Literal[0, 1, 2, 3, 4] = 1,
        save_file: bool | None = None,
    ): ...

    def debug(self, *message: Any, additional_info: bool = True, **kwargs) -> None: ...
    def info(self, *message: Any, additional_info: bool = True, **kwargs) -> None: ...
    def warning(self, *message: Any, additional_info: bool = True, **kwargs) -> None: ...
    def error(self, *message: Any, additional_info: bool = True, **kwargs) -> None: ...
    def critical(
        self,
        *message: Any,
        additional_info: bool = True,
        exception_type: Type[Exception] = Exception,
        **kwargs,
    ) -> None: ...
