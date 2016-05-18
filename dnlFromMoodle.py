# download script for courses that are organized in moodle
# original by vinaychandra (https://github.com/vinaychandra/Moodle-Downloader)
#
# Author: Patrick Nisble

import http.cookiejar as cookielib
#import urllib2
import urllib

import os
import os.path
import re

import configparser
from bs4 import BeautifulSoup


# create configparser for saved credentials and moodle location
conf = configparser.ConfigParser()

# !!!!!! make shure your credentials are saved in the working directory !!!!!!
project_dir = os.getcwd()
#print(project_dir)
conf.read(os.path.join(project_dir, 'moodleconfig.ini'))
root_directory = conf.get("dirs", "save_dir")
username = conf.get("auth", "username")
password = conf.get("auth", "password")
authentication_url = "https://"+conf.get("auth", "url")

# Store the cookies and create an opener that will hold them
cj = cookielib.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

# Add our headers
opener.addheaders = [('User-agent', 'Moodle-Crawler')]

# Install our opener (note that this changes the global opener to the one
# we just made, but you can also just call opener.open() if you want)
urllib.request.install_opener(opener)

# Input parameters we are going to send
payload = {
    'username': username,
    'password': password
}

# Use urllib to encode the payload
data = urllib.parse.urlencode(payload)
data = data.encode('utf8')

# Build our Request object (supplying 'data' makes it a POST)
#req = urllib.request.Request(authentication_url, data)

# Make the request and read the response
print(authentication_url,username[:2])
page = urllib.request.urlopen(authentication_url, data).read()
soup = BeautifulSoup(page,'lxml')
links = soup.find_all("div",class_="activityinstance")

for elem in links:
   
    if "assign" in str(elem.get('href')):
        print(elem.get('href'))
        #rq.urlretrieve(uni_url + elem.get('href'),
        #    "/home/patrick/Downloads/%s-" % key + elem.contents[0])

