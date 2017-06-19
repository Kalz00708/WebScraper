import sys
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
for i in range(1, len(sys.argv)):
    '''
    There are two main things that can go wrong in urlopen
    1. The page is not found
    2. The server is not found
    '''
    # html = urlopen(sys.argv[i])
    try:
        html = urlopen(sys.argv[i])
    except HTTPError as e:
        print(e)
    except URLError as e:
        print(e)
    else:
        if html is None:
            print("URL is not found")
        else:
            print(html.read())
