from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser
from typing import Any, Self
from pydantic import BaseModel
from pydantic_core import PydanticUndefined


class CliArgs(BaseModel):
    @classmethod
    def from_cli_arguments(cls) -> Self:
        ap = cls._parser_from_pydatic()
        raw = ap.parse_args()
        return cls(**vars(raw))

    @classmethod
    def _parser_from_pydatic(cls) -> ArgumentParser:
        parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
        for field_name, field_info in cls.model_fields.items():
            default_field = {}
            names = []

            if field_info.default != PydanticUndefined:
                default_field = {"default": field_info.default, "metavar": field_name}
                if field_info.alias:
                    names.append(f"-{field_info.alias[0]}")
                names.append(f"--{field_name.replace('_', '-')}")
            else:
                names.append(field_name)

            parser.add_argument(
                *names,
                help=field_info.description,
                type=field_info.annotation or Any,
                **default_field,
            )
        return parser
