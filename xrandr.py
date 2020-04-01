#! /usr/bin/env python3

import re, sys
import subprocess as sp
import argparse as ap
import screeninfo as si
import time


def identify():
    return si.get_monitors()


def cloned(disps):
    out = []


    return out

if __name__ == "__main__":

    parser = ap.ArgumentParser()
    parser.add_argument(
        "-c", "--cloned",
        dest="cloned",
        action="store_true"
    )
    parser.add_argument(
        "-b", "--bspwm",
        dest="bspwm",
        action="store_true"
    )

    args = parser.parse_args()

    ids = identify()
    idn = [d.name for d in ids]

    if "DP-1" in idn and "DP-2" in idn:
        sp.check_output(["xrandr", "--output", "eDP-1", "--off"])
        sp.check_output(["bspc", "monitor", "eDP-1", "-r"])
        time.sleep(1)

        cmd = ["bspc", "monitor", "DP-1", "-d", *("I II III".split(" "))]
        print(cmd)
        sp.check_output(cmd)

        cmd = ["bspc", "monitor", "DP-2", "-d", *("IV V VI VII VIII IX X".split(" "))]
        sp.check_output(cmd)

    elif "eDP-1" in idn and len(idn)==2:
        cmd = ["bspc", "monitor", None, "-d"]
        cmd[2] = "eDP-1"
        for s in "I II III".split(" "):
            cmd.append(s)
        sp.check_output(cmd)

        cmd = ["bspc", "monitor", None, "-d"]
        cmd[2] = ids[1].name
        cmd[4] = "IV V VI VII VIII IX X"
        sp.check_output(cmd)
    else:
        cmd = ["bspc", "monitor", "eDP-1", "-d", *("I II III IV V VI VII VIII IX X".split(" "))]
        sp.check_output(cmd)
