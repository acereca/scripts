# This Script will find and download all available pdfs for classes PTP4 and PEP4 of SS2016
#
# Author: Patrick Nisble

from bs4 import BeautifulSoup
import urllib.request as rq
from os import listdir

uni_url = "https://uebungen.physik.uni-heidelberg.de"
to_scan = {"PTP4":"/vorlesung/20161/ptp4","PEP4":"/vorlesung/20161/pep4/uebungen"}

dnl_path = ""

fetched = listdir("/home/patrick/Downloads")

already_fetched = []
for item in fetched:
    if item[:4] == "PTP4" or item[:4] == "PEP4":
        already_fetched.append(item[5:])



for key in to_scan:
    p = rq.urlopen(uni_url + to_scan[key]).read()
    soup = BeautifulSoup(p,'lxml')
    links = soup.find_all("a",class_="pdflink")
    for elem in links:
        if "uebungen" in str(elem.get('href')) and elem.get('href')[24:] not in already_fetched:
            print(elem.get('href')[24:])
            rq.urlretrieve(uni_url + elem.get('href'),
                "/home/patrick/Downloads/%s-" % key + elem.contents[0])
