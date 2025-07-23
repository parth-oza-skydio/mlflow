from __future__ import annotations
import typing

from dataclasses import dataclass

import tomli


@dataclass
class Config:
    exclude: typing.List[str]
    # Path -> List of modules that should not be imported globally under that path
    forbidden_top_level_imports: typing.Dict[str, typing.List[str]]
    typing_extensions_allowlist: typing.List[str]

    @classmethod
    def load(cls) -> Config:
        with open("pyproject.toml", "rb") as f:
            data = tomli.load(f)
            exclude = data["tool"]["clint"]["exclude"]
            forbidden_imports = data["tool"]["clint"]["forbidden-top-level-imports"]
            typing_extensions_allowlist = data["tool"]["clint"]["typing-extensions-allowlist"]
            return cls(
                exclude,
                forbidden_imports,
                typing_extensions_allowlist,
            )
