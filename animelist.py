from bs4 import BeautifulSoup
import urllib.request as rq

### DEFINITIONS
URL_CATALOG = [""]
site = rq.urlopen("http://anime-joy.tv/").read()
soup = BeautifulSoup(site, 'lxml')

print(soup)
