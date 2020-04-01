#! /usr/bin/env python3

# Written by Patrick Nisblé (@acereca)

import re
import os
import subprocess
import argparse
import youtube_dl as ydl

# setup 
regex_outer = re.compile(r"(?P<uploader>^[^:]+)(\s--|:)\s(?P<rest>[^\[\]]+)(?:\[.+\])*(?:\W+\w\w\w)$")
regex_inner = re.compile(r"(?:(?P<artist>[a-zA-Z0-9 '(),.&_]+)\s-\s)?(?P<title>[a-zA-Z0-9 '(),.&_]+)")

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
    'outtmpl': f"{working_dir}/%(uploader)s -- %(title)s.%(ext)s",
    'playlistend': 40,
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
def generate_id3tag(filepath):

    regex_outer = re.compile(
        r"(?P<uploader>^[^:]+)(\s--|:)\s(?P<rest>[^\[\]]+)(?:\[.+\])*(?:\W+\w\w\w)$")
    regex_inner = re.compile(
        r"(?:(?P<artist>[a-zA-Z0-9 '(),.&_]+)\s-\s)?(?P<title>[a-zA-Z0-9 '(),.&_]+)")
    m = regex_outer.match(f)
    m2 = regex_inner.match(m.group('rest'))

    return {
        "title": m2.group("title"),
        "album": m2.group("title"),
        "artist": m2.group("artist") if m2.group("artist") else m.group("uploader")
    }


dl = [f for f in os.listdir(working_dir) if os.path.isfile(os.path.join(working_dir,f))]
print(f"\n{color_codes['green']}=> Updating id3 info of files in '{working_dir}'{color_codes['reset']}")

print(working_dir)
for f in dl:
    new_tags = generate_id3tag(working_dir + "/" + f)

    cmd = [
        'mid3v2',
        os.path.abspath(working_dir + "/" + f),
        '-t',
        new_tags["title"],
        '-a',
        new_tags["artist"],
        '-A',
        new_tags["album"]
    ]
    subprocess.call(cmd)

print("\nDone.")
print(f"Updated info of {len(dl)} files.")

