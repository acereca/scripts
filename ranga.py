#! /usr/bin/env python3

import feedparser as fp
import bs4
import pathlib
import urllib.request

with open("/home/patrick/.newsboat/urls", 'r') as urlfile:
    urls = urlfile.read().split()


# for url in urls:
    url = urls[0]
    feed = fp.parse(url)

    name=feed['channel']['title']
    print(name)
    print(link:=feed['items'][0]['link'])
    print(sub:="/".join(link.split("/")[5:-1]))
    p = pathlib.Path("/home/patrick/manga/"+name+"/"+sub)
    p.mkdir(parents=True, exist_ok=True)

    req = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0'})
    con = urllib.request.urlopen(req)
    html = con.read()

    soup = bs4.BeautifulSoup(html, 'lxml')
    metas=soup.select("[name*='og:image']")
    imgbase=metas[0]['content'].split("?")[0].split("/")[:-1]
    imgbase[2] = '.'.join(['s'] + imgbase[2].split(".")[1:])
    imgbase = "/".join(imgbase)
    print(imgbase)

    ch = "{:05.1f}".format(int(link.split("/")[-2][1:])-1)
    image=imgbase + f"/{ch}/compressed/f000.jpg"
    print(image)
   req = urllib.request.Request(image, headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0'})
    con = urllib.request.urlopen(req)
    # with open(f"/home/patrick/manga/{name}/{sub}/f000.jpg", 'wb') as img:
        # img.write(con.read())
    # while True:
        # try:
            # req = urllib.request.urlopen(imgbase + f"/{ch}/)
        # except Exception as _:
            # break
    # print(soup.prettify())
