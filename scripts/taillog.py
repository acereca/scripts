from pathlib import Path
from time import sleep
from datetime import datetime
from pydantic import Field
from rich.box import MINIMAL
from rich.live import Live
from rich.table import Table
from .common import CliArgs
from re import compile


class TailLogArgs(CliArgs):
    refresh_rate: int = Field(
        default=4, description="refresh rate of log table in Hz", alias="r"
    )
    cmd_delay: int = Field(
        alias="t", default=1, description="delay between log update readins in s"
    )
    log_file: Path = Field(description="file to monitor")
    lines: int = Field(
        alias="l", default=15, description="number of last lines to show"
    )
    match_expression: str = Field(
        default=".*",
        description="regex pattern to select lines by, optionally can contain capture groups i.e. `(\d+).*` matches any line starting with at least one digit. The pttern needs to match the complete line",
    )
    replace_string: str = Field(
        default="{_line}",
        description="f-string, with named capture groups of match_expression available as variables. Special variable `_line` contains the complete original line",
    )


if __name__ == "__main__":
    cli_args = TailLogArgs.from_cli_arguments()
    print(cli_args)

    regex = compile(cli_args.match_expression)

    tab = Table(box=MINIMAL, show_header=False)
    with open(cli_args.log_file, "r") as reading, Live(
        tab, refresh_per_second=cli_args.refresh_rate, screen=True
    ) as live:
        counter = 0
        lines = []
        while True:
            while line := reading.readline():
                counter += 1
                lines.append((f"{counter:>4d}", line.removesuffix("\n")))

            tab = Table(
                box=MINIMAL,
                show_header=False,
                caption=f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {cli_args.log_file}",
            )
            tab.add_column(justify="right")
            lines = lines[-cli_args.lines :]

            for row, line in lines:
                if match := regex.match(line):
                    to_eval = 'f"' + cli_args.replace_string + '"'
                    new_line = eval(to_eval, {"_line": line}, match.groupdict())
                    tab.add_row(row, new_line)

            live.update(tab)
            sleep(cli_args.cmd_delay)
