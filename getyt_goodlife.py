#!/usr/bin/python3
# This Script will find the stream url
#
# Author: Patrick Nisble

from bs4 import BeautifulSoup
import urllib.request as rq
import sys
import subprocess

channel_url = "https://www.youtube.com/user/SensualMusique1"

r = ["streamlink", "--player=mpv --volume=50", r"youtube.com"] + sys.argv[1:]

p = rq.urlopen(channel_url).read()
soup = BeautifulSoup(p,'html.parser')
links = soup.find_all("a")
for elem in links:
    if isinstance(elem.get('title'), str) and "Good Life Radio" in elem.get("title"):
        r[2] += elem.get('href')
        break

print(r)

subprocess.call(r)
