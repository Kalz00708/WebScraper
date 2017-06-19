from urllib.request import urlopen
# from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import re
import datetime
import random
import socket
import csv

examinedPages = set("")
untestedPages = set()
untestedPages.add("http://www.iplaypy.com/jichu/set.html")
domain = set()
domain.add("iplaypy.com")
random.seed(datetime.datetime.now())
csvFile = open("./domain.csv", 'w+')
counter = 0
try:
    writer = csv.writer(csvFile)
except:
    pass

def getContent(url, interval, iterTime):
    while iterTime > 0:
        try:
            html = urlopen(url, timeout = interval).read()
            return html
        #except (HTTPError, URLError):
            #return None
        except (TimeoutError, socket.timeout):
            iterTime -= 1
            if iterTime == 0:
                return None
        except:
            return None

def getDomain(address):
    domainPart = address.replace("https://", "").replace("http://", "").split("/")
    return domainPart[0]

def getExternalLinks(startPage):
    global untestedPages, examinedPages, domain, writer, counter
    html = getContent(startPage, 10, 5)
    if html is None:
        return None
    else:
        bsObj = BeautifulSoup(html, "html.parser")
        for link in bsObj("a", href=re.compile("^(https://|http://)?[0-9a-zA-Z][0-9a-zA-Z\-\.]*(?:\.(?:com|cn|net|club|org|info|me|cc|tv|mobi|name|wang)).*$")):
            if link.attrs['href'] not in (examinedPages | untestedPages):
                untestedPages.add(link.attrs['href'])
            newDomain = getDomain(link.attrs['href'])
            if newDomain not in domain:
                domain.add(newDomain)
                counter += 1
                try:
                    writer.writerow((counter, newDomain))
                except:
                    pass
                print("New external is: " + newDomain)

def findAndGotoExternal():
    global untestedPages, examinedPages
    try:
        startPage = untestedPages.pop()
        examinedPages.add(startPage)
    except KeyError:
        print("The search is finished")
        return False
    else:
        getExternalLinks(startPage)
        return True

notFinish = True
while notFinish:
    notFinish = findAndGotoExternal()
csvFile.close()
