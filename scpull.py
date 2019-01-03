#! /usr/bin/env python3

# Written by Patrick Nisblé (@acereca)

import re
import os
import subprocess
import argparse
import youtube_dl as ydl

# setup 
regex_outer = re.compile(r"(?P<uploader>^[^:]+): (?P<rest>[^\[\]]+)(?:\[.+\])*(?:\W+\w\w\w)$")
regex_inner = re.compile(r"(?:(?P<artist>[^-]+)(?:\s+-\s+))?(?P<title>.+[^-\s])")

color_codes = {
    'green': '\033[1;32m',
    'reset': '\033[0m'
}

parser = argparse.ArgumentParser()
parser.add_argument(
    "-d", "--dir",
    metavar="directory",
    type=str,
    default="./dnl",
    help="directory to work in, (default: './dnl')"
)

parser.add_argument(
    '-a', '--db-archive',
    metavar='db_file',
    type=str,
    default='./done.db',
    help="reference file for already downloaded files, (default: './done.db')"
)

args = parser.parse_args()
working_dir = args.dir

ydl_n = 0

def hook(d):
    if d['status'] == 'finished':
        global ydl_n
        ydl_n += 1
        print(d['filename'])
    else:
        print('.', end='')

# downloads
ydl_options = {
    'outtmpl': f"{working_dir}/%(uploader)s: %(title)s.%(ext)s",
    'playlistend': 10,
    'quiet': True,
    'writethumbnail': True,
    'download_archive': "./done.db",
    'progress_hooks': [hook],
    'postprocessors': [
        {'key': 'EmbedThumbnail'}
    ]
}

ydl_url = "https://soundcloud.com/dracereca/likes"
print(f"{color_codes['green']}=> Downloading files at '{ydl_url}'{color_codes['reset']}")
with ydl.YoutubeDL(ydl_options) as dl:
    dl.download([ydl_url])

print("Done.")
print(f"Downloaded {ydl_n} new tracks.")

# processing of id3 tags
dl = [f for f in os.listdir(working_dir) if os.path.isfile(os.path.join(working_dir,f))]
print(f"\n{color_codes['green']}=> Updating id3 info of files in '{working_dir}'{color_codes['reset']}")

for f in dl:
    cmd = ['mid3v2', f"{working_dir}/{f}", '-t', '', '-a', '']
    m = regex_outer.match(f)
    uploader = m.group('uploader')
    m2 = regex_inner.match(m.group('rest'))

    if m2.group('artist'):
        cmd[3] = m2.group('artist')
    else:
        cmd[3] = m.group('uploader')

    cmd[5] = m2.group("title")

    subprocess.call(cmd)

print("\nDone.")
print(f"Updated info of {len(dl)} files.")

