#! /usr/bin/env python3

from subprocess import check_output
from re import Pattern, compile
from time import sleep
from typing import TypedDict
from pydantic import Field
from rich.box import HEAVY_HEAD, MINIMAL, Box
from rich.console import JustifyMethod
from rich.table import Table
from rich.live import Live
from .common import CliArgs


class TabulateCliArgs(CliArgs):
    columns: list[str] = Field(default_factory=list)
    parse_expression: str
    cmd: str
    refresh_rate: int = 4
    cmd_delay: int = 2
    small: bool = False


def parse_cmd(cmd: str, expr: Pattern[str]) -> list[tuple[str, ...]]:
    matches = []
    data_input = check_output(cmd.split()).decode().split("\n")
    for line in data_input:
        matched = expr.match(line)
        if matched:
            matches.append(matched.groups())

    return matches


def new_table(args: TabulateCliArgs) -> Table:
    class CommonTableSettings(TypedDict):
        title: str
        min_width: int
        title_justify: JustifyMethod
        box: Box
        pad_edge: bool

    common_tab_settings = CommonTableSettings(
        title=f"cmd: '{args.cmd}'\nrefresh rate: {args.refresh_rate}Hz, cmd execution delay: {args.cmd_delay}s",
        min_width=60,
        title_justify="left",
        box=HEAVY_HEAD,
        pad_edge=True,
    )

    if args.small:
        common_tab_settings["box"] = MINIMAL
        common_tab_settings["title"] = ""
        common_tab_settings["pad_edge"] = False
        common_tab_settings["min_width"] = 0

    if args.columns:
        tab = Table(**common_tab_settings)
        for col in args.columns:
            tab.add_column(col)
        return tab

    return Table(show_header=False, **common_tab_settings)


if __name__ == "__main__":
    cli_args = TabulateCliArgs.from_cli_arguments()
    tab = new_table(cli_args)
    regex = compile(cli_args.parse_expression)

    with Live(tab, refresh_per_second=cli_args.refresh_rate, screen=True) as live:
        while True:
            tab = new_table(cli_args)
            for match in parse_cmd(cli_args.cmd, regex):
                tab.add_row(*match)

            live.update(tab)
            sleep(cli_args.cmd_delay)
