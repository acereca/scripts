# This Script will find and download all available pdfs for classes PTP4 and PEP4
#
# Author: Patrick Nisble
#

from bs4 import BeautifulSoup
import urllib.request as rq

uni_url = "https://uebungen.physik.uni-heidelberg.de"
to_scan = {"PTP4":"/vorlesung/20161/ptp4","PEP4":"/vorlesung/20161/pep4/uebungen"}

dnl_path = ""

for key in to_scan:
    p = rq.urlopen(uni_url + to_scan[key]).read()
    soup = BeautifulSoup(p,'lxml')
    links = soup.find_all("a",class_="pdflink")
    for elem in links:
        if "uebungen" in str(elem.get('href')):
            print(elem.get('href')[24:])
            rq.urlretrieve(uni_url + elem.get('href'),
                "/home/patrick/Downloads/%s-" % key + elem.contents[0])
