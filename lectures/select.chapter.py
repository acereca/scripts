#! /usr/bin/env python3
import subprocess
import rofi
import os
import os.path
import glob
import yaml
import time

aln = os.path.expanduser("~") + "/University/LectureNotes/active"
max_name_len = 0
# create possible combinations
selectable = [{"path": fp} for fp in glob.glob(aln + "/*.md")]

for f in selectable:
    with open(f['path']) as of:
        try:
            docs = yaml.safe_load_all(of)
            for d in docs:
                if isinstance(d, dict):
                    f['title'] = d.get('title', '-').rstrip()
                    max_name_len = max([len(f['title']), max_name_len])
                    f['index'] = d.get('index', '-')
                    if d.get('created', None) is not None:
                        f['ctime'] = d.get('created', None)
                    else:
                        f['ctime'] = time.ctime(os.path.getctime(f['path']))
                    f['ctime'] = '<span gravity="east" weight="ultralight" size="15000" style="italic">' + f['ctime'] + '</span>'
                    break
        except Exception as _:
            f['title'] = os.path.splitext(os.path.basename(f['path']))[0]

for f in selectable:
    # padding
    f['ctime'] = ((4 +max_name_len-len(f['title']))  * " ") + f['ctime']

selectable = sorted(selectable, key=lambda item: -item['index'] if item['index'] else 0)
selectable.insert(0, {'title': '~new~', 'index': len(selectable)})
# rofi selection
r = rofi.Rofi()
# take the lecture title from README.md title in TOML
i, key = r.select(
    'open a "' + selectable[-1]['title'] + '" Chapter',
    ["{:3d}".format(s['index'])+ ": " + s['title'] + s.get('ctime', "") for s in selectable],
    rofi_args=['-markup-rows']
)

if key == 0:
    if i == 0:
        print(aln + "/" + r.text_entry('new Chapter No. ' + str(len(selectable)-1) + ' Filename?') + ".md")
    else:
        print(selectable[i]['path'])
