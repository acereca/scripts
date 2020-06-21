#! /usr/bin/env python3
import rofi
import bibtexparser as bib
import sys, glob, os, subprocess

ubib_dir = "~/github/ubib"
viewer = "evince"

def filelist(d=ubib_dir):
    aln = os.path.expanduser(d)
    fullnames = glob.glob(aln + "/**/*.pdf")
    names = [f[len(aln)+1:] for f in fullnames]
    return {n.split("/")[1].split(".")[0]:{
        'src': n,
        'cat': n.split("/")[0]
    } for n in names}

with open(os.path.expanduser(ubib_dir) + "/ubib.bib") as bf:
    bib_data = bib.load(bf)

kk = [e['ID'] for e in bib_data.entries]
f = filelist()
for k in f:
    for i, kv in enumerate(kk):
        if kv == k:
            f[k]['name'] = bib_data.entries[i]['title']
            f[k]['auth'] = bib_data.entries[i]['author']

r = rofi.Rofi()

ll = sys.argv*2
if ll[1] not in f:
    i, key = r.select(
        "UBIB Selection",
        [f'{e["auth"]}: "{e["name"]}" ({e["cat"]}, "./{e["src"]}")' for _,e in f.items()],
        rofi_args=['-i']
    )
else:
    i = list(f.keys()).index(sys.argv[1])
    key = 0

fs = os.path.expanduser(ubib_dir) + "/" + f[list(f.keys())[i]]['src']
print(i, fs)

if key == 0:
    subprocess.Popen(
        [viewer, fs]
    )
