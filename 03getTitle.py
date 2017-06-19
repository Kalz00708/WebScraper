import sys
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    except URLError as e:
        return None

    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.find("body").find("h1") # title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

for i in range(1, len(sys.argv)):
    title = getTitle(sys.argv[i])
    if(title == None):
        print("Title could not be found")
    else:
        print(title)
