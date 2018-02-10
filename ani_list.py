#! /bin/usr/python3

from bs4 import BeautifulSoup
import urllib.request as rq
import sys
import re

if len(sys.argv) not in [3, 4]:
    sys.exit("\nwrong number of arguments!\n\nUsage: ani_list.py URL_OF_1ST NUMS_OF_EPS [OUTFILE]")

result = []
outfile = "dnllist.out" if len(sys.argv) == 3 else sys.argv[3]
print(sys.argv)
for i in range(1, int(sys.argv[2])+1):
    print('.',end='')
    # opne intial site and find button
    site = rq.urlopen(sys.argv[1][:-1] + str(i))
    b = BeautifulSoup(site, 'html.parser')
    links = b('span', class_="btndownload")

    # open secondary site and find downloadable content
    secondary = links[0].parent.get("href")
    req = rq.Request(
        str(secondary),
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )
    sec_site = rq.urlopen(req)

    b = BeautifulSoup(sec_site, 'html.parser')
    out = ''
    for l in b(text=re.compile(r'Openload')):
        out = l.parent.get('href')

    if out == '':
        #sys.exit("did not find downloadable link for link no. " + str(i))
        out = "#missing for " + str(i)

    result.append(out)

print(result)

with open(outfile, 'w') as f:
    for line in result:
        f.write(line + "\n")
