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


# CONFIG

# path to moodelconfig.ini
config_dir = "/home/patrick/Downloads/"


#####################################

# create configparser for saved credentials and moodle location
conf = configparser.ConfigParser()

# test for given project_path
if config_dir == "":
    project_dir = sys.getcwd()
else:
    project_dir = config_dir

print(project_dir)

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
contents = urllib.request.urlopen(authentication_url, data).read()

courses = contents.split("<h2>My courses</h2>")[1].split('<aside id="block-region-side-pre" ')[0]

regex = re.compile('<h3 class="coursename">(.*?)</h3>')
course_list = regex.findall(courses)
courses = []

for course_string in course_list:
    soup = BeautifulSoup(course_string)
    a = soup.find('a')
    course_name = a.text
    course_link = a.get('href')
    courses.append([course_name, course_link])

for course in courses:
    if not os.path.isdir(root_directory + course[0]):
        os.mkdir(root_directory+course[0])
    response1 = urllib2.urlopen(course[1])
    scrap = response1.read()
    soup = BeautifulSoup(scrap)

    course_links = soup.find(class_="course-content").find(class_="weeks").find_all('a')

    for link in course_links:
        current_dir = root_directory + course[0] + "/"
        href = link.get('href')

        # Checking only resources... Ignoring forum and folders, etc
        if "resource" in href:
            cj1 = cookielib.CookieJar()
            opener1 = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj1))

            # Add our headers
            opener1.addheaders = [('User-agent', 'Moodle-Crawler')]

            # Install our opener (note that this changes the global opener to the one
            # we just made, but you can also just call opener.open() if you want)
            urllib2.install_opener(opener1)

            # The action/ target from the form
            authentication_url1 = href

            # Build our Request object (supplying 'data' makes it a POST)
            req1 = urllib2.Request(authentication_url, data)

            # Make the request and read the response
            resp = urllib2.urlopen(req1)

            webFile = urllib2.urlopen(href)
            url = current_dir + webFile.geturl().split('/')[-1].split('?')[0]
            file_name = urllib.unquote(url).decode('utf8')
            if os.path.isfile(file_name):
                print("File found : ", file_name)
                continue
            print("Creating file : ", file_name)
            #pdfFile = open(file_name, 'wb')
            #pdfFile.write(webFile.read())
            webFile.close()
            #pdfFile.close()
print("Update Complete")
