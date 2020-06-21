#! /usr/bin/env python3
import argparse
import os.path
import subprocess

p = argparse.ArgumentParser()

p.add_argument('-r', dest='relative', action='store_true')
p.add_argument('-m', dest='mul', action='store_true')
p.add_argument('brightness', type=float, nargs=1)

args = p.parse_args()

filep = os.path.expanduser('~/.config/xrandr/backlight')

bl = 0
if args.relative:
    with open(filep) as f:
        bl = float(f.read())

    bl *= float(subprocess.check_output(['light', '-G']))

    bl += args.brightness[0]
elif args.mul:
    with open(filep) as f:
        bl = float(f.read())

    bl *= float(subprocess.check_output(['light', '-G']))

    bl *= args.brightness[0]
else:
    bl = args.brightness[0]

if bl < 0:
    bl = 0
if bl > 100:
    bl = 100

## now do processing
if bl < 1:
    subprocess.check_output(['xrandr', '--output', 'eDP-1', '--brightness', str(bl)])
    subprocess.check_output(['light', '-S', str(1)])
    with open(filep, 'w') as f:
        f.write(str(bl))
else:
    subprocess.check_output(['xrandr', '--output', 'eDP-1', '--brightness', str(1)])
    subprocess.check_output(['light', '-S', str(bl)])
    with open(filep, 'w') as f:
        f.write(str(1))
