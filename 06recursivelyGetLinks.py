from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import re, socket

pages = set()

def getContent(url, interval, iterTime):
    while iterTime > 0:
        try:
            html = urlopen("http://en.wikipedia.org" + url, timeout = interval). read()
            return html
        except (HTTPError, URLError):
            return None
        except (TimeoutError, socket.timeout):
            iterTime -= 1
            if iterTime == 0:
                return None

def getLinks(pageUrl):
    global pages
    # use to count the time if timeout, give the program 5 times to try
    html = getContent(pageUrl, 10, 5) 
    if html is None:
        return None

    bsObj = BeautifulSoup(html, "html.parser")
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id="mw-content-text").findAll("p")[0])
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs["href"])
    except AttributeError:
        print("This page is missing something! No worries though!")

    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
        if link.attrs['href'] not in pages:
            newPage = link.attrs['href']
            print("---------------\n" + newPage)
            pages.add(newPage)
            getLinks(newPage)

getLinks("")
