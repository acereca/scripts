#! /usr/bin/env python3
import subprocess
import rofi
import os
import os.path
import glob
import argparse

p = argparse.ArgumentParser()

p.add_argument(
    '--unix',
    '-u',
    dest="unix",
    action="store_true",
    help="output into pipable format"
)

args = p.parse_args()

# define semester to show
active_sem = "WiSe1920"
ln = os.path.expanduser("~") + "/University/LectureNotes/"
# create possible combinations
selectable = glob.glob(ln + active_sem + "/*")

if args.unix:
    for s in selectable:
        print(s)
else:
    # rofi selection
    r = rofi.Rofi()
    i, key = r.select('Change active Lecture to', [
        '<span gravity="east" weight="ultralight" size="15000" style="italic">' + active_sem + '/ </span>' +
        s.split("/")[-1] for s in selectable
    ],
                      rofi_args=['-markup-rows'])

    if key == 0:
        os.remove(ln + "active")
        os.symlink(selectable[i], ln + "active")
