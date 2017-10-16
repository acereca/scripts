#!/usr/bin/python3
# This Script will find the stream url
#
# Author: Patrick Nisble

from bs4 import BeautifulSoup
import urllib.request as rq
import sys
import subprocess
import youtube_dl

channel_url = "https://www.youtube.com/" + sys.argv[1]

r = ["youtube-dl -g", r"youtube.com"] + sys.argv[3:]

p = rq.urlopen(channel_url).read()
soup = BeautifulSoup(p,'html.parser')
links = soup.find_all("a")
for elem in links:
    if isinstance(elem.get('title'), str) and sys.argv[2] in elem.get("title"):
        r[1] += elem.get('href')
        break

print(r[1])