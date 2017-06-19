from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import re

try:
    html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
except HTTPError as e:
    print(e)
except URLError as e:
    print(e)
else:
    if html is None:
        print("page is not exist")
    else:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        if bsObj is None:
            print("no content")
        else:
            for link in bsObj.find("div", {
                "id":"bodyContent"
                }).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
                print(link.attrs['href'])
