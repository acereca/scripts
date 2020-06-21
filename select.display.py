#! /usr/bin/env python3
import subprocess
import rofi
import os.path

def cmd_xrandr(primary, secondary, expansion=None):
    out = ['xrandr', '--output', primary, '--primary', '--auto', '--output', secondary]
    out_name = ''
    if expansion == 'same':
        out[5] = '--same-as'
        out_name = '='
    elif expansion == None:
        out.append('--off')
        out_name = 'x'
    elif expansion in ['left', 'right', 'above', 'below']:
        out.append('--auto')
        out.append('--' + expansion)
        if expansion in['left', 'right']:
            out[-1] += '-of'
        out.append(primary)

        out_name = secondary + ' ' + expansion + ' of ' + primary

    return {'name': out_name, 'cmd': out}

# parse xrandr for display names
output = subprocess.Popen('xrandr | grep " connected"',shell=True, stdout=subprocess.PIPE).communicate()[0]
displays = [n.split()[0].decode() for n in output.strip().split(b'\n')]

# create possible combinations
selectable = []

for di in [None, 'same', 'left', 'right', 'above', 'below']:
    selectable.append(cmd_xrandr(displays[0], displays[1], di))

# rofi selection
r = rofi.Rofi()
i, key = r.select('Screen Setup', [s['name'] for s in selectable])

if key == 0:
    # prevent not connecting to external display
    if i == 1:
        subprocess.call(selectable[3]['cmd'])
    subprocess.call(selectable[i]['cmd'])
    # relaod polybar
    subprocess.call(["/bin/sh", "/home/patrick/.config/bspwm/bspwmrc", "&", "disown"])
    # reapply bg
    subprocess.call(['feh', '--bg-fill', '/home/patrick/Pictures/bg_i3', '--no-xinerama'])
