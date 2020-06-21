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

    pos = {
        "DP2": ["--left-of", "eDP1"],
        "DP1": ["--left-of", "DP1"]
    }

    ws = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]

    # split screen between all connected (and open) monitors
    if "eDP1" in idn and "open" not in str(sp.check_output(["cat", "/proc/acpi/button/lid/LID0/state"])):
        sp.check_output(["xrandr", "--output", "eDP1", "--off"])
        sp.check_output(["bspc", "monitor", "eDP1", "-r"])
        del idn[idn.index("eDP1")]

    for i, mon in enumerate(idn):
        if mon != "eDP1":
            sp.check_output(["xrandr", "--output", mon, pos[mon][0], pos[mon][1]])

        dw = len(ws)//len(idn)
        sp.check_output(["bspc", "monitor", mon, "-d", *ws[i*dw:(i+1)*dw]])

    if "eDP1" in idn:
        del idn[idn.index("eDP1")]

    # if "DP-1" in idn and "DP-2" in idn:
        # sp.check_output(["xrandr", "--output", "eDP-1", "--off"])
        # sp.check_output(["bspc", "monitor", "eDP-1", "-r"])
        # time.sleep(1)

        # cmd = ["bspc", "monitor", "DP-1", "-d", *("I II III".split(" "))]
        # print(cmd)
        # sp.check_output(cmd)

        # cmd = ["bspc", "monitor", "DP-2", "-d", *("IV V VI VII VIII IX X".split(" "))]
        # sp.check_output(cmd)

    # elif "eDP1" in idn and len(idn)==2:
        # cmd = ["bspc", "monitor", None, "-d"]
        # cmd[2] = "eDP1"
        # for s in "I II III".split(" "):
            # cmd.append(s)
        # sp.check_output(cmd)

        # cmd = ["bspc", "monitor", None, "-d"]
        # cmd[2] = ids[1].name
        # cmd[4] = "IV V VI VII VIII IX X"
        # sp.check_output(cmd)
    # else:
        # cmd = ["bspc", "monitor", "eDP1", "-d", *("I II III IV V VI VII VIII IX X".split(" "))]
        # sp.check_output(cmd)
